# 🔍 NFT Trend Scanner

**Decentralized NFT Market Trend Oracle — Built on GenLayer**

## Overview

An Intelligent Contract on Testnet Bradbury that scans live NFT marketplace data and uses AI consensus to identify trending collections and market sentiment.

## Features

- Fetches live NFT market data via gl.nondet.web.render
- AI identifies top trending collections and scores market heat (0-100)
- Classifies market sentiment: BEARISH, NEUTRAL, BULLISH
- Decentralized consensus via Optimistic Democracy

## Why GenLayer

This project is impossible on any other blockchain — it requires native web access to scan NFT marketplaces, NLP to interpret unstructured listing data, and AI consensus simultaneously.

## Deploy

1. Open GenLayer Studio: https://studio.genlayer.com/contracts
2. Paste `01_nft_trend_scanner.py`
3. Constructor Input: `scan_url` = `https://www.coingecko.com/en/nft`
4. Deploy → Execute `scan_trends`

## Tech Stack

- Python GenVM SDK
- gl.nondet.web.render for live data
- gl.nondet.exec_prompt for AI analysis
- gl.eq_principle.strict_eq for consensus

## License

MIT
