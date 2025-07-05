import type { NextApiRequest, NextApiResponse } from 'next';
import { executeIQCL } from '../../utils/iqcl';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }
  const { input } = req.body;
  const output = executeIQCL(input || '');
  res.status(200).json({ output });
}