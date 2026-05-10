/**
 * EarnNexus Auto-Verification Engine
 * Connects Bank/PayFast signals to User Permissions.
 */

export const VerificationEngine = {
  /**
   * Called when a webhook or bank-scraper detects a matching Reference ID.
   */
  async verifyAndUnlock(orderId: string, amountReceived: number) {
    console.log(`🔍 Verifying Payment for Order: ${orderId}...`);

    // 1. Validate against the Database (Supabase)
    const { data: order, error } = await supabase
      .from('orders')
      .select('*')
      .eq('id', orderId)
      .single();

    if (order && amountReceived >= order.total_price) {
      // 2. Flip the 'is_paid' and 'access_granted' flags
      await supabase
        .from('users')
        .update({ 
          status: 'ACTIVE', 
          access_level: 'PRO',
          unlocked_at: new Date().toISOString() 
        })
        .eq('id', order.user_id);

      console.log(`✅ Access Granted for User: ${order.user_id}. Platform features UNLOCKED.`);
      
      // 3. Trigger Bronwyn to send a "Welcome/Success" notification
      BronwynAgent.notifySuccess(order.user_id);
      return true;
    }
    return false;
  }
};
