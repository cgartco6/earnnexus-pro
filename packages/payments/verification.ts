import { supabase } from '../db/client';
import { BronwynAgent } from '../../apps/agents/bronwyn';

export const EFTVerification = {
  async processPayment(orderId: string, amount: number, reference: string) {
    // 1. Verify payment against reference in evolution_history
    const { data: order, error } = await supabase
      .from('orders')
      .select('*')
      .eq('payment_reference', reference)
      .single();

    if (order && amount >= order.total_price) {
      // 2. AUTO-UNLOCK: Update user status to ACTIVE
      await supabase.from('users').update({ 
        is_active: true, 
        access_unlocked: true 
      }).eq('id', order.user_id);

      // 3. LOG & NOTIFY: Bronwyn sends the success link
      console.log(`[VERIFIED] Order ${orderId} unlocked.`);
      BronwynAgent.notifyUnlock(order.user_id, order.product_type);
      return true;
    }
    return false;
  }
};
