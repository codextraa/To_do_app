import "@/styles/globals.css";


export const metadata = {
  title: "TODO APP",
  description: "Todo App created by Next.js and Django",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}
