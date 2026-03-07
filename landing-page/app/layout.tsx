import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'MFM Presentations | Open-Source Maternal-Fetal Medicine Education',
  description:
    "The world's leading open-source library of 80+ evidence-based clinical presentations and interactive tools for MFM, created by Dr. Chukwuma Onyeije.",
  openGraph: {
    title: 'MFM Presentations | Open-Source Maternal-Fetal Medicine Education',
    description:
      'Evidence-based clinical presentations and tools for patients, providers, and sonographers.',
    url: 'https://mfm-presentations.vercel.app',
    siteName: 'MFM Presentations',
    images: [
      {
        url: 'https://mfm-presentations.vercel.app/og-image.png',
        width: 1200,
        height: 630,
        alt: 'MFM Presentations - Open-Source Maternal-Fetal Medicine Education',
      },
    ],
    locale: 'en_US',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'MFM Presentations | Open-Source Maternal-Fetal Medicine Education',
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
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
