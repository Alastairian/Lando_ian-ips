import Head from 'next/head';
import LandoConsole from '../components/LandoConsole';

export default function Home() {
  return (
    <>
      <Head>
        <title>Lando - IAI-IPS Quantum Cognition Chat</title>
      </Head>
      <main className="min-h-screen bg-gray-900 text-white flex items-center justify-center p-4">
        <div className="w-full max-w-2xl">
          <h1 className="text-2xl font-bold mb-4 text-center">Lando - IAI-IPS Quantum Cognition Chat</h1>
          <LandoConsole />
        </div>
      </main>
    </>
  );
}