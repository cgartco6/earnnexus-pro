import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: true,
  images: {
    domains: ["payfast.co.za", "stripe.com"],
  },
  // Security headers for POPIA/GDPR
  async headers() {
    return [{
      source: "/(.*)",
      headers: [{ key: "X-Frame-Options", value: "DENY" }]
    }];
  }
};

export default nextConfig;
