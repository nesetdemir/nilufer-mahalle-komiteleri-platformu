import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Nilüfer Mahalle Komiteleri Platformu',
  description: 'Mahalle komitelerinin karar alma ve duyuru platformu',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="tr">
      <body>{children}</body>
    </html>
  )
}
