# Huzur

**Appointments by lottery, not by speed.** ("Randevu hıza değil, kuraya göre.")

*Huzur* is Turkish for "presence" and "peace of mind". Fair public draws in Turkey are announced as held "noter huzurunda", in the presence of a notary. Here the chain is the notary: the draw happens in everyone's presence, and nobody has to refresh a booking page at midnight.

Huzur distributes scarce appointments (starting with visa appointments) through a lottery that anyone can verify on Monad, instead of "first come, first served". Bot speed buys nothing, the operator cannot pick the winners, and a won appointment is bound to the applicant's passport without putting any personal data on chain.

> **Türkçe özet:** Huzur, kıt randevuları "ilk gelen alır" yerine herkesin doğrulayabildiği bir kurayla dağıtır. Bot hızı bir şey kazandırmaz, kurayı işleten sonucu seçemez, kazanılan randevu pasaporta bağlıdır; zincirde kişisel veri yoktur.

Built at Monad Blitz Ankara v4 (October 24, 2026).

## Live demo

- App: [Vercel URL]
- Projector view: [Vercel URL]/perde
- Verify a finished draw without our server: [Vercel URL]/dogrula?b=[example batch id]
- API health: [Render URL]/health

## Contracts (Monad testnet, chain ID 10143)

| Contract | Address | Source |
| --- | --- | --- |
| `Huzur` | [address] | Verified on [MonadVision link] |
| `IlkGelen` (demo of today's first-come system) | [address] | Verified on [MonadVision link] |

Deployed on October 24, 2026 at block [number], commit [hash].

## The problem

[Two or three sentences with sources from `docs/urun-ozeti.md`: bots grab visa appointments within seconds and resell them for 300–500 EUR; 60 detention orders in Turkey in October 2026.]

## How it works

1. **Open.** The operator opens a batch and commits to a secret seed by publishing only its hash. The closing block is announced up front.
2. **Apply.** The phone creates a random salt and a commitment `keccak256(passportNo, salt)`. The server checks eligibility, derives a one-per-passport nullifier with HMAC and signs an EIP-712 eligibility message. A relayer writes the entry on chain, so applicants need no wallet and no MON.
3. **Close and draw.** After the closing block, its block hash is fixed as entropy. The operator reveals the seed, and the contract runs a partial Fisher-Yates shuffle over the commitments.
4. **Verify.** `/dogrula` recomputes the draw in the browser from chain data only and checks the seed, the entropy and the winner list.
5. **Gate.** At the appointment, the gate device recomputes the commitment from the passport number and the salt on the applicant's ticket. A resold ticket does not match the buyer's passport.

[Architecture diagram from `docs/teknik-plan.md`]

## Why it needs a chain

[Seed committed before entries, entropy from a block nobody controls, draw executed by the contract, anyone can recompute the result, one passport one entry. No payments on chain. Why Monad: appointment openings are traffic bursts; 0.3 s blocks and 0.6 s finality make the live draw instant.]

## Privacy and security

- No passport number, name or photo on chain: only salted commitments and HMAC nullifiers.
- The passport photo never leaves the gate device; the server only sees the commitment there.
- Roles are split (`OPERATOR_ROLE`, `SIGNER_ROLE`, `GATE_ROLE`); the admin key is not on the server. No proxy, no payable functions, no external calls.
- Claude writes a plain-language explanation of each draw from public numbers only and cannot affect the result.
- [Threat model summary from `docs/teknik-plan.md`]

## Run it locally

[Prerequisites, then contracts (`forge test`), server (`uvicorn`), web (`npm run dev`), environment variables from the `.env.example` files.]

## What is not finished

- Identity verification is mocked: the demo uses generated passport numbers. A real deployment would read the e-passport chip (ICAO 9303).
- [Anything else that is not working yet, stated plainly.]

## Business model

The organisation that hands out appointments or tickets pays per application; applicants apply for free. Payment stays off chain in local currency. The same engine fits hajj lotteries, public housing draws and derby tickets.

## Prepared before coding started

Disclosed per the Blitz rules ("Built at the event · disclose prior work"):

- The idea, market research and design documents: `docs/teknik-plan.md`, `docs/urun-ozeti.md`, `docs/marka.md`, `docs/calisma-duzeni.md`. The design document contains short reference snippets (hash definitions, the draw loop, an EIP-712 signing example) and test vectors.
- Claude Code configuration and helper scripts: `CLAUDE.md`, `.claude/settings.json`, `scripts/session-start.sh`, `scripts/cloud-setup.sh`, `scripts/export-abi.sh`, `scripts/make_keys.py` (testnet key generator).
- Deployment and environment templates: `render.yaml`, `web/vercel.json`, `.env.example` files, `.gitignore`, this README skeleton.

No application code (contracts, server, web) existed before the event. All of it was written on October 24, 2026; see the commit history.

## Built with

Solidity and Foundry, OpenZeppelin, FastAPI, Vite, React and viem, Monad testnet, Vercel, Render, Claude API. Code written with Claude Code.

## License

MIT
