import type { Metadata } from 'next';
import { Inter, Space_Grotesk } from 'next/font/google';
import './globals.css';

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
  weight: ['300', '400', '500', '600'],
});

const spaceGrotesk = Space_Grotesk({
  subsets: ['latin'],
  variable: '--font-space-grotesk',
  weight: ['400', '500', '600', '700'],
});

export const metadata: Metadata = {
  title: 'openMFM | Open-Source Maternal-Fetal Medicine Education',
  description:
    "The world's first open-source education platform for Maternal-Fetal Medicine. 80+ evidence-based clinical presentations and interactive tools for patients, providers, and sonographers. Created by Dr. Chukwuma Onyeije, MD.",
  openGraph: {
    title: 'openMFM | Open-Source Maternal-Fetal Medicine Education',
    description:
      'Evidence-based clinical presentations and tools for patients, providers, and sonographers.',
    url: 'https://mfm-presentations.vercel.app',
    siteName: 'openMFM',
    images: [
      {
        url: 'https://mfm-presentations.vercel.app/og-image.png',
        width: 1200,
        height: 630,
        alt: 'openMFM - Open-Source Maternal-Fetal Medicine Education',
      },
    ],
    locale: 'en_US',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'openMFM | Open-Source Maternal-Fetal Medicine Education',
    description:
      'The open-source library for high-risk pregnancy topics, from preeclampsia to fetal cardiology.',
    images: ['https://mfm-presentations.vercel.app/og-image.png'],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`${inter.variable} ${spaceGrotesk.variable}`}>
      <body>{children}</body>
    </html>
  );
}
