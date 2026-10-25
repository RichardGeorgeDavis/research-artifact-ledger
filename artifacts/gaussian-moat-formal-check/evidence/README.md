# Retained evidence and reproduction boundary

Published 2026-10-12. The five machine-output files are byte-for-byte copies of retained run outputs and the check input. Build and axiom hashes match the earlier mechanical review receipts. This packaging pass did not rerun Lean. SHA256SUMS identifies those published bytes; it does not authenticate cached binaries against source, certify execution time or prove discovery priority. A later read-only [compatibility-patch audit](dependency-patch-audit-20261012.md) records the tracked-diff comparison separately.

The [bounded source-audit update](source-audit-update-20261012.md) records three later source-level reviews and a report-only challenge. These reviews add no machine outputs and did not run Lean or Lake.

The [2026-10-16 source-audit update](source-audit-update-20261016.md) records three additional bounded source-review interfaces, including endpoint conversion, an inverse-limit application and an accurate-band application. It is a summary of retained review records, not a fresh proof audit or reproduction; full proof assurance remains open.

The [2026-10-18 source-audit update](source-audit-update-20261018.md) records three further bounded Mathlib declaration reviews and a separate source-map challenge. These reviews add no machine outputs and did not run Lean or Lake.

## Claim-to-evidence map

| Claim | Evidence | Limit |
|---|---|---|
| Main target completed | [lake-build.log](lake-build.log), final two lines | Cached dependencies were used; 8,964 jobs does not mean 8,964 fresh source compilations |
| Endpoint and axiom list printed | [theorem-axioms.txt](theorem-axioms.txt) | Recorded output under the declared imported environment |
| Exact query | [kernel-check.lean](kernel-check.lean) | Input, not an independent checker |
| Runtime identities | [toolchain.txt](toolchain.txt), [lake-version.txt](lake-version.txt) | Runtime self-report |
| File integrity | [SHA256SUMS](SHA256SUMS) | Integrity only, not authenticity or timestamp certification |

## Environment and reproduction

Upstream source: `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` in `openai/math`, project directory `lean`. Lean 4.34.1, Linux ARM64; Lake version appears in the retained output. Recorded image: `docker.io/library/buildpack-deps@sha256:5c622c484a937f524bb2d8a2bf7fb1a45ce77fda7b56d20fe1fdf7bdff35f69a`. The final run used a 7 GiB guest limit, disabled networking, read-only toolchain/package-cache inputs and a writable project/result mount. These containment details come from the execution record, not the five machine-output files alone.

The pinned upstream `lean/lake-manifest.json` has recorded SHA-256 `cf6105a25d9dca2f166b241d9191bd12c7e13305890dc9c4d0952351cccc0794`; Mathlib revision is `d13f23b723b8a846827a245b89c10fc7d3f11612`. The prior audit recorded 42 matching dependency revisions/origins. No complete per-file cache manifest is published or source authentication claimed.

From the pinned project's `lean` directory, with its declared toolchain and reviewed dependencies prepared, copy the supplied check file into that directory and run:

```sh
lake build OAI.NumberTheory.GaussianMoat.Main
lake env lean kernel-check.lean
```

These are reproduction instructions, not a verbatim shell transcript of the original container launch. Dependency preparation may require network access and executes Lake hooks; the original target run used an already prepared cache offline. This bundle is not a self-contained environment image.

## Warnings, failure and missing receipts

Both logs preserve all eleven local-dependency-change warnings. The pinned Lake configuration declares the compatibility patches. A scoped audit compared each of the eleven retained tracked package diffs with its corresponding pinned patch: all eleven passed `git apply --reverse --check`, and the complete tracked diff content matched the patch after normalising only abbreviated-versus-full Git index-hash lines. This explains the tracked source changes that produced those warnings. The check did not inventory ignored cache contents or authenticate compiled `.olean` bytes against source. Do not treat patch identity as cache provenance.

The execution record states that the build wrapper failed after Main succeeded because it referenced `/result/project/kernel-check.lean` instead of `/result/kernel-check.lean`. A separate offline invocation produced the retained axiom output. Numeric exit-status receipts and the original wrapper stderr are not included in these retained files; no numeric values have been reconstructed. A future independent reproduction should capture commands, stdout, stderr and exit codes separately.

## Review and chronology

The previous AI-assisted consistency review did not rerun Lean or the comparator, and was not independent human certification. Its requested model settings were not runtime-verifiable. The comparator configuration permits the reported axiom set; the comparator harness was not run. Complete transitive proof review remains open.

The ledger entry first appeared in commit [b506310](https://github.com/RichardGeorgeDavis/research-artifact-ledger/commit/b506310c4540bdc6cfc6db3f2f33feff0830b91f). This bundle appears later. Git metadata records repository chronology but is not a certified timestamp or proof of first conception. The theorem is attributed to OpenAI; this ledger records our bounded check.
