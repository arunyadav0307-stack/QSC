# Research-Paper Blueprint

## Exact Marker Capacity of Quantum Synchronizable Codes: optimal classical payload of synchronization syndromes and a multiplicative synchronization–information trade-off

> **What this is.** This is a blueprint for one paper, not the paper itself. The paper has one central contribution: an exact, closed-form answer to the question "how many classical messages can the synchronization marker of a cyclic-code quantum synchronizable code (QSC) carry, for a given misalignment tolerance?" A synchronizable hybrid-code construction attains this number, and its consequences are drawn out, including the resolution of the open trade-off conjecture of Tansuwannont–Nemec.
>
> **Status labels used throughout.** Every claim carries one of these labels.
> - **[E]** Established in the literature. The exact source is cited (paper, theorem, or equation) from the 12 corpus papers in `Quantum Synchronizable.zip`, or from a reference named in a corpus paper's bibliography.
> - **[C]** Computed and verified in this project. A script path in `blueprint/verify/` and an output file in `blueprint/results/` are given. Run `verify/run_all.sh` to reproduce in about 20 s with pure Python 3.
> - **[N]** A new result proposed here. Its proof status is stated: *proof sketch complete*, *to prove*, or *numerically supported only*.
> - **[O]** Open, or depends on material not available. The item needed is named in §18.
>
> Nothing here uses a paper, dataset, or value that was not actually read or computed. Where the published version of a source differs from the version available, this is marked [O].

---

## 1. Proposed title

**"Exact Marker Capacity of Quantum Synchronizable Codes and Optimal Synchronizable Hybrid Codes from Nested Cyclic Codes"**

(Alternative short title for a letter version: *"How Much Classical Information Can a Quantum Synchronization Marker Carry?"*)

Target venues (Q1/SCI): IEEE Trans. Inf. Theory, IEEE Trans. Quantum Eng. (where the closest prior work, T–N, is published [E, see §19]), Quantum Inf. Process., Des. Codes Cryptogr., or Cryptogr. Commun. (which published 2 of the corpus QSC papers).

---

## 2. Research problem

**Setting.** Fujiwara's QSCs [P2] and their algebraic refinement by Fujiwara–Tonchev–Wong [P3] take two binary cyclic codes C ⊂ D of length n. C is dual-containing (C^⊥ ⊆ C). They build a CSS code from C, apply an X-type "marker" X(g) with g ∈ D∖C, and pad the block with a_l + a_r qubits by CNOTs.

When the receiver's window is misaligned by θ ∈ {−a_l, …, a_r}, measuring the Z-type parity checks of D and C gives a **synchronization syndrome**. From it, θ is recovered [E: P2 Thm 1; P3 §II]. Across the corpus, the syndrome is used to recover θ only. Recovering θ only is the single purpose of the marker in [P2, P3, P5–P12].

Tansuwannont–Nemec [P4] showed that the same measurements can also deliver classical bits. They replace X(q_1) by X(q_1 + Σ_{m=2}^{y+1} c_m q_m), which gives y "Z-side" classical bits [E: P4 Thm 5 item 4, Lemma 3]. The cost is a linear loss of tolerance: a_l + a_r < k_D − k_C − y. They show r + m + d_sync,max = 2(k_D − k_C) for their whole family [E: P4 Cor 2] and **conjecture that this sum is optimal** [E: P4 §7].

**Problem.** Fix C ⊂ D as above, with κ := k_D − k_C = deg f and f := g_C/g_D.

1. What is the **maximum number N_f(L) of distinct classical messages** the marker can carry while every misalignment in a window of L = a_l + a_r + 1 positions stays correctable? The quantum parameters [[n + a_l + a_r, 2k_C − n]], the bit/phase-error correction, and the measured operators must all be unchanged.
2. What is the **true trade-off** between classical payload and synchronization distance? Is the T–N conjecture correct?
3. Can the optimum be **attained by an explicit, efficiently decodable** synchronizable hybrid code? Does this extend to q-ary and repeated-root QSC families from the corpus?

---

## 3. Source-paper synthesis

Paper keys [P1]–[P12] are used throughout; full references are in §19. "Tolerance" means the guaranteed a_l + a_r.

| Key | Paper | Construction / method | Tolerance result | Classical info? | Validation used in paper |
|---|---|---|---|---|---|
| P2 | Fujiwara, PRA 87 (2013) 022344 | First QSC. Nested cyclic C ⊂ D, C dual-containing, CSS plus marker X(g), CNOT padding | a_l + a_r < k_D − k_C [E: Thm 1]. Corrects ⌊(d_C−1)/2⌋ phase and ⌊(d_D−1)/2⌋ bit errors | no | proofs; examples (BCH, Hamming-type) |
| P3 | Fujiwara–Tonchev–Wong, PRA 88 (2013) 012318 | Algebraic analysis of the marker via f = g_C/g_D in F_2[x]/(f) | **a_l + a_r < ord(f)** [E: Thm 4, with Props 6/18 for general n]. Dual-containing BCH criterion [E: Thms 12/13, quoted from their ref. [16]]. Punctured RM families [E: Lemma 9, Thm 10]. Prime Mersenne lengths give tolerance n [E: Thm 14]. d_C − d_D ≥ 4 gives full tolerance n [E: Thm 17] | no | proofs plus explicit parameter lists |
| P7 | Xie–Yuan–Fujiwara, ITW 2014 | QR codes and augmented QR codes of Mersenne-prime length p = 2^l − 1 | (c_l, c_r)-[[p + c_l + c_r, 2zl + 1]] for c_l + c_r < p [E: Thm 4.5] | no | proofs |
| P6 | Du–Ma–Luo–Huang–Wang, IEEE Access 8 (2020) 8449 | (λ(u+v)\|u−v) with repeated-root constacyclic codes | maximum tolerance claimed | no | examples |
| P8 | Li–Zhu, IJTP 61 (2022) 251 | cyclotomic polynomials at prime length; negacyclic BCH on (u+v\|u−v) | "best attainable" under conditions | no | examples |
| P9 | Shi–Yue–Huang, Cryptogr. Commun. 13 (2021) 727 | Whiteman generalized cyclotomy; factorizations of Φ_{p1p2}(x) | best attainable tolerance claimed | no | tables (Ex. 2 / Table 4, q = 29, n = 35) |
| P11 | Liu–Kai, JAMC 69 (2023) 1751 | three BCH families; **exact** minimum distances | best achievable tolerance | no | Ex. 3.10 [[80 + a_l + a_r, 52]]_9 |
| P10 | Wang–Zhou, Cryptogr. Commun. 17 (2025) 1427 | BCH of length (q^m − 1)/a with explicit minimum distance | maximum tolerance | no | Ex. [[124 + a_l + a_r, 106]]_5 |
| P12 | Du–Ma–Liu, Comput. Appl. Math. 42 (2023) 161 | repeated-root **quasi-cyclic** codes | tolerance via QC structure | no | examples (internal consistency not re-checked, see §15) |
| P4 | Tansuwannont–Nemec, arXiv:2409.11312v2 (published IEEE TQE 7 (2026) 2100730, [O] version not read) | Stabilizer-formalism reformulation of QSCs; **synchronizable hybrid subsystem codes** Q1–Q7; general CSS-type hybrid/subsystem constructions (Thms 8–10) | Q3: κ classical bits, d_sync = κ. Q4: κ + y bits, d_sync = κ − y. Q6: y bits, κ gauge qubits [E: Thm 5]. **Cor 2**: r + m + d_sync,max = 2κ. **Conjecture** of optimality [E: §7] | **yes (first)** | proofs; lookup-table decoding (Lemma 3) |
| P5 | Nemec–Klappenecker, arXiv:1911.12260v2 | general theory of hybrid quantum-classical codes; impurity; weight enumerators and LP bounds; families of genuine hybrid codes (d = 2, 3) via unions of stabilizer-code translates | — | hybrid framework | proofs, LP computations |
| P1 | La Guardia, QIC 11 (2011) 239 | asymmetric quantum BCH codes (d_z/d_x) | not a QSC paper; supplies the asymmetric CSS viewpoint used in §6 | no | parameter tables |

**Methods that recur across the corpus** [E]:
- (M1) Cyclic or constacyclic nested pairs C ⊂ D, with C dual-containing.
- (M2) The tolerance is governed by ord(f), and the best possible tolerance equals n or the block length [P3; P7–P11].
- (M3) Families are produced by choosing defining sets from cyclotomic cosets [P3, P8–P11].
- (M4) Minimum distances are computed or bounded [P10, P11].
- (M5) T–N alone uses the stabilizer and hybrid formalism and trades tolerance for classical bits [P4].

**Limitations identified.**
- (L1) **Every family paper [P2, P3, P6–P12] optimizes only the tolerance for a single marker.** None asks how much information the marker coset can carry.
- (L2) The T–N marker family is **affine and degree-based**: u = 1 + Σ c_m x^{m−1} with deg u ≤ y. Their Lemma 3 argues independence of shifts from degrees, which gives a tolerance κ − y. It ignores ord(f), which by [P3] can be much larger than κ (for example ord(f) = 31 for κ = 5).
- (L3) The T–N optimality conjecture is stated without proof and without an information-theoretic converse.
- (L4) The q-ary families [P8–P11] are never evaluated as hybrid codes.
- (L5) Validation across the corpus is by proof plus hand-worked examples. No paper supplies reproducible code. In one case (P9, Table 4) the stated tolerance appears inconsistent with the ord(f) criterion; see §15. This is to be re-verified and is not a contribution.

---

## 4. Precise research gap

> **Gap.** For a QSC built from nested cyclic codes C ⊂ D, the synchronization marker is an element of the quotient module D/C. The marker's **classical capacity** under a tolerance constraint (the maximum number of markers such that every (marker, misalignment) pair gives a distinct syndrome) has **never been determined**. The only known construction, T–N's affine degree-based family, achieves 2^{κ−L} messages at window L ≤ κ. This leads to the additive trade-off r + m + d_sync = 2κ, which T–N conjecture to be optimal. No upper bound, no exact value, and no construction for L > κ with more than one marker is known in the corpus or in the literature we could find (web search results recorded in §18).

Why this is a genuine gap and not a restatement:
- [P3] determines the maximum window for **one** marker (ord f).
- [P4] gives **one** family of multi-marker sets with a linear penalty.
- The quantity N_f(L) interpolates between these two, and neither paper computes it.
- The numbers show the gap is large. For BCH63-b at window L = 63, the optimum carries **64 messages (6 bits)**, while the T–N family carries no Z-side bits for any L > κ = 12. For BCH31-c at L = 5, it carries **198 messages versus T–N's 32** [C: `results/tables.md`, T2].

---

## 5. Novel contribution (single central result)

**Central contribution:** an exact **marker-capacity theorem** for cyclic-code QSCs, together with a matching **synchronizable hybrid-code construction** that achieves it. The capacity is

N_f(L) = [L = 1] + Σ_{g | f, g ≠ 1} (Φ_q(g) / ord(g)) · ⌊ord(g) / L⌋,

with an explicit cyclotomic-coset form. These are four facets of one result, not four contributions:

1. **(Theorem A, capacity.)** Exact formula for N_f(L), valid for any prime power q and any f | x^n − 1 with repeated roots allowed. It includes a converse (necessity of admissibility) for all decoders that use computational-basis information of the window.
2. **(Theorem B, attainment.)** An explicit (a_l, a_r)-((n + a_l + a_r, 2^{2k_C − n} : N_f(L), d ≥ d_D)) synchronizable hybrid code. It has *the same* quantum parameters, measurements, and error-correction radii as Fujiwara/FTW. It can be combined with T–N's X-side bits.
3. **(Theorem C, trade-off.)** The true trade-off is **multiplicative**: |M| · d_sync ≤ q^κ − 1. This bound is tight (with an explicit tightness criterion). Consequently the additive T–N quantity r + m + d_sync exceeds 2κ for broad families. This resolves the T–N conjecture in the negative, including within stabilizer (affine) hybrid codes (explicit certified instance).
4. **(Theorem D, decoding.)** Encoding and decoding need zero additional quantum operations. For irreducible f, the classical post-processing is one discrete logarithm in F_{q^κ}^× plus integer arithmetic.

**Why this is not copying, renaming, or merely combining sources.**
- [P3] studies only |M| = 1.
- [P4] only has affine, degree-limited M.
- Theorem A is a new extremal result: an orbit-packing problem in R_f = F_q[x]/(f) solved exactly, with a converse.
- Theorem C refutes a published conjecture.
- The construction reuses source validation (FTW syndrome algebra, T–N Theorem 7 shift-invariance), as the task asks.

---

## 6. Mathematical framework

**Standing assumptions** (label [E] where from the sources).
- (A1) q is a prime power, n ≥ 2. C = ⟨g_C⟩ ⊂ D = ⟨g_D⟩ are cyclic codes of length n over F_q, so g_D | g_C | x^n − 1. Set f := g_C / g_D and κ := deg f = k_D − k_C ≥ 1 [E: P2, P3].
- (A2) Binary case (quantum part): C^⊥ ⊆ C, so CSS(C) = [[n, 2k_C − n]] with X-distance and Z-distance ≥ d_C [E: P2, P4]. The q-ary case uses the corresponding Euclidean/Hermitian dual-containing CSS constructions of [P8–P11]. The quantum part of the q-ary Theorem B is [O] (see §8).
- (A3) Misalignment model of [P2, P4]: the receiver's n-qubit window is shifted by θ ∈ {−a_l, …, a_r} relative to the true block. Pauli errors act on the (padded) block.
- (A4) The sync measurement is the set of Z-type checks of D and C on the window, that is Z(q̃_i) and Z(p̃_j) in T–N's notation [E: P4 §3.2, eq. (56); P2].

**The key algebraic object.** R_f := F_q[x]/(f). Because f | x^n − 1, gcd(x, f) = 1, so T : R_f → R_f, u ↦ x·u is a permutation (an F_q-linear automorphism of order ord(f)) [standard; ord(f) as in P3].

**Lemma 1 (quotient isomorphism) [N, proof complete; trivial].** The map ι : R_f → D/C, u ↦ u·g_D + C, is an F_q[x]-module isomorphism. In particular, x-multiplication on D/C corresponds to T.
*Proof.* ι is well defined because f g_D = g_C. It is surjective since D = {a g_D}. If u g_D ∈ C then g_D f | u g_D, so f | u. Dimensions agree (κ).

**Lemma 2 (window syndrome) [N, generalization of E].** With marker w_u := u·g_D (u ∈ R_f) and misalignment θ, the combined outcome of the window's C-checks, after D-correction of ≤ t_D := ⌊(d_D − 1)/2⌋ bit flips, is the class s = x^{−θ} u ∈ R_f, independent of the logical state.
*Source:* This is FTW's computation with g replaced by u·g_D (P3 §II; P4 eq. (56)). It is verified in the label-level simulation [C: `verify/simulate.py`, `results/simulation.txt`].

**Admissibility.** A marker set M ⊆ R_f is *L-admissible* if the map M × {0, …, L−1} → R_f, (u, a) ↦ x^a u, is injective. The sign and offset convention is immaterial, because T is a bijection and the window [−a_r, a_l] is a translate of [0, L−1].

**Capacity.** N_f(L) := max{|M| : M is L-admissible}.

**Totient and order.**
- Φ_q(g) := |(F_q[x]/(g))^×|.
- ord(g) := min{e ≥ 1 : g | x^e − 1}.
- For irreducible p of degree d, Φ_q(p^k) = q^{d(k−1)}(q^d − 1). Φ_q is multiplicative, and ord(p^k) = ord(p) · char^t with t minimal such that char^t ≥ k [E: Lidl–Niederreiter, Thm 3.8. The book is cited as ref. [12] in P3, which uses its Thms 3.9, 3.16, 3.20 and Cor. 3.4. The book itself is [O] in the workspace].

**Cyclotomic data (gcd(n, q) = 1).**
- If f = Π_{i∈I} M_i is squarefree (M_i the minimal polynomial of α^i), then d_i := |C_i| (the q-cyclotomic coset) and e_i := ord(M_i) = n / gcd(i, n).
- For S ⊆ I, e_S := lcm_{i∈S} e_i.

---

## 7. Definitions and notation

| Symbol | Meaning |
|---|---|
| C ⊂ D | nested cyclic codes [n, k_C, d_C] ⊂ [n, k_D, d_D] |
| f, κ | f = g_C / g_D, κ = deg f = k_D − k_C (T–N write this as k_d − k_c) |
| R_f, T | F_q[x]/(f); multiplication by x |
| w_u | marker word u(x) g_D(x) mod x^n − 1, u ∈ R_f |
| a_l, a_r, L | left and right tolerance; window L := a_l + a_r + 1 (= T–N's d_sync,max when tight) |
| M | marker (classical message) set, M ⊆ R_f |
| N_f(L) | marker capacity (§6) |
| O | an orbit (cycle) of T on R_f; e_O = \|O\| |
| Q_CSS | CSS(C) = [[n, 2k_C − n]] |
| ((N, K : M, d)) | hybrid code of length N with K-dimensional quantum part, M classical messages, distance d (NK notation [P5]). T–N write [[N, k : m, d]] with m = log2 M bits |
| m_X | number of T–N "X-side" classical bits, encoded by Z(Σ b_m q_m) into X-stabilizer phases [E: P4 §5, Q3] |
| r | number of gauge qubits in T–N (not used for κ, to avoid a clash) |
| [L = 1] | Iverson bracket |

**Definition (marker-hybrid QSC).**
- For an L-admissible M with L = a_l + a_r + 1, encode (|ψ⟩, u) ↦ Pad_{a_l, a_r}(X(w_u) · Enc_CSS(|ψ⟩)), where Pad is the CNOT padding of [P2]/[P4 Thm 5, step 3].
- Optionally apply T–N's X-side operator Z(Σ b_m q_m) before X(w_u).
- The code space is Q_M := ⊕_{u∈M} Pad(X(w_u) Q_CSS).

---

## 8. Main theorem / conjecture targets

### Theorem A (exact marker capacity) — [N], proof sketch complete (§9)

Under (A1), for every L ≥ 1:

(A-i) **Orbit-packing form.** N_f(L) = Σ_{orbits O of T} ⌊e_O / L⌋. For L ≥ 2 the orbit {0} contributes 0.

(A-ii) **Divisor form.** N_f(L) = [L = 1] + Σ_{g | f, g monic, g ≠ 1} (Φ_q(g) / ord(g)) · ⌊ord(g) / L⌋.

(A-iii) **Cyclotomic form** (squarefree f, gcd(n, q) = 1). N_f(L) = [L = 1] + Σ_{∅ ≠ S ⊆ I} (Π_{i∈S}(q^{d_i} − 1) / e_S) · ⌊e_S / L⌋.

(A-iv) **Converse, Z-basis decoders.** If M is not L-admissible, then every decoder whose input is the outcome of any computational-basis measurement of the n window qubits misidentifies (u, θ) with probability ≥ 1/2 for some pair of hypotheses under uniform prior. The logical input |+⟩^{⊗(2k_C − n)} suffices. This class contains the syndrome decoders of [P2, P3, P4].

(A-v) **Sufficiency.** An L-admissible M is decodable from the syndrome s by table lookup, or by the normal-form decoder of Theorem D.

**Corollaries** [N; proof complete given A]:
- **A1:** N_f(L) ≤ ⌊(q^κ − 1)/L⌋ for L ≥ 2, with equality **iff** Σ_O (e_O mod L) < L.
- **A2 (uniform orbits):** if every nonzero u has orbit size e (for example n prime and f | (x^n − 1)/(x − 1), so e = n), then N_f(L) = ((q^κ − 1)/e) · ⌊e/L⌋.
- **A3 (recovers FTW):** max{L : N_f(L) ≥ 1} = ord(f) [E: P3].
- **A4 (lower bound):** N_f(L) ≥ (q^κ − 1 − (L − 1)·#orbits)/L. So log2 N_f(L) ≥ κ log2 q − log2 L − o(1) whenever #orbits · L ≪ q^κ.

**Verification status [C].**
- (A-i) = (A-ii) = CRT form = (A-iii), across 4 independent implementations (`orbits.py`). There were 0 mismatches on 59 random f and on all benchmark instances, including repeated-root f and q ∈ {2, 3, 5, 29}. The cyclotomic form was cross-checked against polynomial brute force on 11 cases.
- Optimality (the converse inside R_f) is verified independently by an exact maximum-independent-set computation on the confusability graph. The graph is built from the definition only, with no orbit theory (`mis_check.py` → `results/mis_check.txt`: **ALL OK**).

### Theorem B (optimal synchronizable hybrid codes) — [N], to prove (proof strategy in §9; binary case)

Let q = 2 and assume (A1)–(A4). Let M be L-admissible with L = a_l + a_r + 1 ≤ ord(f) (for example M an optimal set of size N_f(L)).

(B-i) Q_M is an (a_l, a_r)-((n + a_l + a_r, 2^{2k_C − n} : |M|, d)) synchronizable hybrid code with d ≥ d_D. It is asymmetric in La Guardia's sense [P1]: X-distance ≥ d_D, Z-distance ≥ d_C.

(B-ii) It corrects every misalignment θ ∈ [−a_l, a_r], up to t_D bit flips, and up to ⌊(d_C − 1)/2⌋ phase flips. The guarantees are the same as Fujiwara's Thm 1 [E: P2]. It recovers **both θ and u**.

(B-iii) **Compatibility with T–N.** Adding T–N's X-side encoding Z(Σ_{m=1}^{m_X} b_m q_m), m_X ≤ κ, yields ((n + a_l + a_r, 2^{2k_C − n} : |M| · 2^{m_X}, d_D)). With m_X = κ and M = {1}, L = κ, this is exactly T–N's Q3 [E: P4 Thm 5.3]. The affine M of Lemma 3 gives Q4.

(B-iv) **Quantum resources.** The encoder differs from FTW/T–N only in the depth-1 Pauli layer X(w_u). The measured operators are identical. So the extra log2|M| classical bits cost zero extra quantum gates or measurements.

(B-v) **q-ary version** [O]: the same statement for the q-ary CSS constructions used in [P8–P11]. It requires the qudit CSS/hybrid formalism (Ketkar et al. 2006, cited as [18] in P5), which is listed in §18. The capacity part (Theorem A) is already q-ary and verified [C: T4].

### Theorem C (multiplicative synchronization–information trade-off) — [N]

(C-i) **Converse** (Z-basis decoders, from A-iv): any marker set carried by the C-syndrome satisfies |M| · L ≤ q^κ − 1 for L ≥ 2. In bits: log2|M| + log2 d_sync ≤ log2(q^κ − 1) < κ log2 q.

(C-ii) **Achievability.** N_f(L) attains (C-i) exactly iff the criterion of Cor. A1 holds. Otherwise it is within #orbits · (L − 1)/L messages (Cor. A4).

(C-iii) **T–N conjecture.** T–N's additive accounting r + m + d_sync,max, where m counts all classical bits, is **not** bounded by 2κ.
- (a) *Elementary instance:* Theorem B with M = {1}, m_X = κ, L = ord(f) gives κ + ord(f) > 2κ whenever ord(f) > κ. This is FTW's ord(f) tolerance combined with T–N Q3; B-iii must be proven for it.
- (b) **Proposition C2** [N, proof complete, see §9; numerically checked for all primes 7 ≤ n < 600, 57,384 cases, 0 failures, `results/prop_uniform.txt`]: in the uniform-orbit case (binary, n prime ≥ 7), log2 N_f(L) + L > κ for every 2 ≤ L ≤ κ. So even inside T–N's tolerance regime L ≤ κ, the optimal markers beat the additive frontier y + d_sync = κ.
- (c) *Within stabilizer (affine) hybrid codes and integer bits:* for BCH31-b ([31,16,7] ⊂ [31,21,5], κ = 5), the affine marker set x² + span{1 + x⁴, x + x³} is 5-admissible [C: `tn_counterexample.py`, 4000/4000 decoder checks]. So y = 2 Z-side bits at d_sync = 5, and with m_X = 5 the sum is r + m + d_sync = 0 + 7 + 5 = 12 > 2κ = 10. T–N's Lemma 3 construction gives y + d_sync ≤ 5.

(C-iv) **Additive capacity (secondary, partly open).** Let y_aff(L) be the maximum dimension of an admissible affine subspace. Then y_aff(L) ≤ ⌊log2 N_f(L)⌋. Exhaustive computation for κ ≤ 6 shows y_aff(L) ≥ κ − L + 1 for L ≥ 4 in the tested instances [C: `results/affine.txt`]. A general formula for y_aff is [O] and is stated as a conjecture/open problem, not a main claim.

**Caveat.** The published TQE version of T–N [O] may phrase the conjecture differently, for example restricting the code class. The blueprint states (C-iii) against the arXiv v2 wording ("We conjecture that the sum of the numbers obtained by our code construction is optimal", §7). This must be re-checked against the published version before submission.

### Theorem D (encoding/decoding complexity) — [N], to prove; irreducible-f case

Let f be irreducible of degree κ with e = ord(f). Then R_f ≅ F_{q^κ}, x ↦ β of order e, and the orbits of T on R_f^× are the cosets of ⟨β⟩. Choose a primitive γ with γ^{(q^κ − 1)/e} = β. An optimal marker set is

M* = {γ^i β^{jL} : 0 ≤ i < (q^κ − 1)/e, 0 ≤ j < ⌊e/L⌋}.

- **Encoding** a message (i, j) costs O(κ² log q^κ) field operations.
- **Decoding** from s = x^{−θ} u: take ℓ = log_γ s. Then i = ℓ mod (q^κ − 1)/e and k = (ℓ − i)/((q^κ − 1)/e) ≡ jL − θ (mod e). Next k' = (k + a_r) mod e, j = ⌊k'/L⌋, θ = jL + a_r − k'. This is one discrete logarithm (Pohlig–Hellman, polynomial in the largest prime factor of q^κ − 1) plus O(1) integer operations. For κ ≤ 24 a table of size q^κ suffices.
- For **general squarefree f** the orbit ranking via CRT, supports S, and the diagonal subgroup ⟨(β_i)_{i∈S}⟩ is [O] as a closed-form efficient bijection. The table-lookup decoder is always available and is implemented (`simulate.py` uses the orbit normal form).

### Remark R (benchmark hygiene, not a contribution)

In [P9] Ex. 2 / Table 4 (q = 29, n = 35), the claimed tolerance a_l + a_r < 35 conflicts with the ord(f) criterion. The factor f = x − α^{20} has ord(f) = 7, because α has order 35. So FTW's criterion gives < 7, and Cor. A3 gives max L = 7 [C: T4]. This is to be re-verified from the paper's exact definitions before any mention. If confirmed, it is noted neutrally in the benchmark section.

---

## 9. Proof strategy

**Theorem A.**
1. *Reduction to R_f.* Use Lemma 1 (D/C ≅ R_f) and Lemma 2 (syndrome = x^{−θ}u). Sufficiency (A-v) is immediate: if (u, θ) ↦ x^{−θ}u is injective on M × window, a lookup table inverts it.
2. *Converse (A-iv).*
   - Take the logical input |+⟩^{⊗k}. Its CSS codeword is Σ_{c∈C} |c⟩, since C^⊥ ⊆ C.
   - With padding by CNOT copies, every computational-basis label of the extended block reads, on any n consecutive positions, a cyclic shift of the label. This is the property used in [P2, P4].
   - So the window's Z-basis distribution under (u, θ) is uniform on x^{−θ}w_u + C. Here C is cyclic and bit-flip noise acts identically.
   - If x^{−θ}u ≡ x^{−θ'}u' (mod f), Lemma 1 shows the two cosets coincide, so the two distributions are identical.
   - Any Z-basis decoder then errs with probability ≥ 1/2 on that pair.
   - Status: sketch complete; write out with explicit padding indices from P4 eqs. (73)–(77).
   - Extending the converse to *arbitrary* quantum measurements on the window (mixed bases) is [O]. It is plausibly true by twirling over logical Paulis, but it is not claimed.
3. *Packing.* Admissibility ⇔ the L-arcs A_u = {u, xu, …, x^{L−1}u} are pairwise disjoint and each has exactly L elements, which forces e_{O(u)} ≥ L. Disjoint L-subsets of a cycle of length e number at most ⌊e/L⌋. The bound is attained by u, x^L u, x^{2L} u, …. Sum over cycles to get (A-i).
4. *Orbit census.* For u ≠ 0 let h = gcd(u, f) and g = f/h. Then x^a u ≡ u (mod f) ⇔ g | (x^a − 1)·(u/h) ⇔ g | x^a − 1, since u/h is a unit mod g. So e_{O(u)} = ord(g). The map u ↦ (u/h mod g) is a bijection from {u : f/gcd(u, f) = g} onto (F_q[x]/(g))^×, so there are Φ_q(g) such u, forming Φ_q(g)/ord(g) orbits. Substituting gives (A-ii).
5. *Cyclotomic form.* Use CRT and ord(Π_{i∈S} M_i) = lcm_{i∈S} e_i with e_i = n/gcd(i, n) (standard; used in P3, P9–P11). Use Φ_q(Π M_i) = Π(q^{d_i} − 1).
6. *Corollaries.*
   - A1: Σ_O⌊e_O/L⌋ = (q^κ − 1 − R)/L with R = Σ(e_O mod L), and R ≡ (q^κ − 1) (mod L).
   - A4: use ⌊x⌋ ≥ x − (L − 1)/L termwise.

**Proposition C2 (proof, complete).** Take binary, uniform orbits e = n prime ≥ 7, κ = deg f ≥ 3 (κ is a multiple of ord_n(2) ≥ 3), 2 ≤ L ≤ κ ≤ n − 1. We need N · 2^L > 2^κ with N = ((2^κ − 1)/n) ⌊n/L⌋.
- *L = 2:* N · 4 = 2(2^κ − 1)(n − 1)/n > 2^κ ⇔ (1 − 2^{−κ})(1 − 1/n) > 1/2. This holds for n ≥ 7, κ ≥ 3.
- *3 ≤ L ≤ n/2:* ⌊n/L⌋ ≥ n/(2L), so N · 2^L ≥ (2^κ − 1) 2^{L−1}/L ≥ (4/3)(2^κ − 1) > 2^κ.
- *n/2 < L ≤ n − 1:* ⌊n/L⌋ = 1 and 2^L ≥ 2^{(n+1)/2} > 2n for n ≥ 7, so N · 2^L > 2(2^κ − 1) ≥ 2^κ.

**Theorem B.**
1. *Hybrid structure.* The inner codes X(w_u)Q_CSS are the joint eigenspaces of the Z(p̃_j) with eigenvalues (−1)^{p̃_j · w_u}. Distinct u give distinct cosets w_u + C (Lemma 1), hence distinct eigenvalue patterns, hence mutually orthogonal subspaces. This is the same mechanism as T–N's inner codes, eqs. (73)–(77).
2. *Distance.*
   - A Pauli E of weight < d_D, written as X-part e_X plus Z-part e_Z, has e_X ∉ D ∖ {0}. So either e_X is detected by the D-checks, or e_X = 0.
   - e_Z of weight < d_C is detected by the X(p̃) checks or acts trivially, since C^⊥ ⊆ C and d_C ≥ d_D.
   - Transitions between messages would need e_X ∈ (w_u − w_{u'}) + C ⊆ D ∖ C, which has weight ≥ d_D.
   - Conclude using NK's hybrid detection conditions [P5, Def. of hybrid code / error detection].
3. *Synchronization.*
   - T–N **Theorem 7** [E] states that, for arbitrary binary v, w and all −a_l ≤ α ≤ a_r, the shifted operators (78)–(80) generate the same stabilizer group.
   - Apply it with w = w_u, the marker, and v the X-side word.
   - This yields that after misalignment the window measurements return x^{−θ}u (Lemma 2), and that recovery proceeds as in T–N §5.2 once (u, θ) are decoded.
   - The only step of T–N's proof that uses the specific marker is Lemma 3 (injectivity). Replace it by admissibility.
4. *Error correction.* Take bit and phase correction verbatim from [P2 Thm 1] / [P4 §5]. The marker is X-type and known after decoding, so it commutes with all X-stabilizer measurements.
5. *Deliverable.* Write a self-contained proof in the T–N stabilizer notation. Risk: the padding and index bookkeeping; this is mitigated by a stabilizer simulation, §10(V4).

**Theorem C.** (C-i) is (A-iv) plus Cor. A1. (C-ii) is Cor. A1/A4. (C-iii)(a) follows from Theorem B. (C-iii)(b) is Prop. C2. (C-iii)(c) is an explicit certificate checked by exhaustive decoding [C].

**Theorem D.** Use the standard structure of F_{q^κ}^× (cyclic) and uniqueness of the subgroup of order e. Discrete-log cost follows from Pohlig–Hellman (a standard reference must be added, §18). Correctness: the decode map is the inverse of the encode map on the window, by Theorem A's packing.

---

## 10. Computational / algorithmic methodology

All the following are already implemented (pure Python 3, `blueprint/verify/`) unless marked "planned".

- **(V1) Four independent capacity computations** (`orbits.py`):
  - (a) brute-force orbit census of T on R_f;
  - (b) the divisor formula (A-ii) with ord computed by factoring f (repeated roots via Lidl–Niederreiter);
  - (c) CRT form;
  - (d) the cyclotomic-coset-only form (A-iii), valid for any prime power q, which needs no field arithmetic.
  - Agreement of (a)–(d) is the primary numerical check [C].
- **(V2) Definition-level optimality check** (`mis_check.py`): build the confusability graph (u ~ v iff their L-arcs intersect, or u has a short orbit) directly from the definition. Compute the exact maximum independent set per connected component and compare with N_f(L) [C: ALL OK, binary n ∈ {7, 14, 15, 21} and q = 3 cases, including repeated roots].
- **(V3) Label-level decoder simulation** (`simulate.py`): random codeword c ∈ C, marker w_u from the optimal set, Fujiwara padding, misalignment θ uniform in [−a_l, a_r], up to t_D random bit flips, then D-decoding, C-syndrome, and the orbit-normal-form decoder. Success means exact (u, θ) [C: 3000/3000 for every tested (instance, L)].
  - *Justification of label-level adequacy:* all sync measurements are Z-type, so every basis label in the superposition yields the same outcomes (P4 §3.2).
  - Phase errors and logical fidelity are *not* simulated here; see V4.
- **(V4) Stabilizer-level simulation** (planned; requires `stim`, not installed, [O]):
  - Build the full Clifford encoder (CSS encoder, X(w_u), CNOT padding) for the n = 31 instances. Apply the misalignment as a qubit-window selection and code-capacity depolarizing noise. Measure Z(q̃_i), Z(p̃_j), and the X-stabilizers, decode, realign, and check logical Pauli frames.
  - Target: the logical failure rate equals that of the FTW single-marker code within statistical error at every noise level. The classical message error equals 0 for weight ≤ t_D.
- **(V5) Additive-vs-nonadditive analysis** (`affine.py`): exhaustive enumeration of affine subspaces for κ ≤ 6. Also the exact maximal window of the T–N family itself, to separate the gain from (i) using ord(f) instead of degrees and (ii) allowing non-affine M [C: `results/affine.txt`].
- **(V6) Certificates** (`tn_counterexample.py`, `prop_uniform.py`) [C].
- **(V7) Benchmark tables** (`tables.py`) [C].
- **(V8) Planned extensions:**
  - n = 255 BCH pairs, via cyclotomic formula (instant) and brute force up to κ ≤ 24 (C re-implementation recommended).
  - Repeated-root instances from [P6] and [P12].
  - Exact d(C) for BCH127-b ([127, 99], currently OPEN) via Magma/Sage or a Gray-code enumeration of the 2^28-word dual.

---

## 11. Validation and reproducibility plan

1. **Reproduce published values first (pipeline validation).**
   - The pipeline must reproduce each source's stated tolerance as max{L : N_f(L) ≥ 1} = ord(f):
     - FTW BCH/Mersenne examples [P3];
     - XYF QR p = 31 → 31 [P7] [C];
     - Wang–Zhou n = 124, q = 5 → 124 [P10] [C];
     - Liu–Kai n = 80, q = 9 → 80 [P11] [C];
     - Li–Zhu and Du et al. examples [P6, P8] (to add; data are in the corpus PDFs).
   - Any mismatch is investigated before using that source as a benchmark (for example Remark R for [P9]).
2. **Independent-method agreement:** V1 (a)–(d), and V2 versus Theorem A.
3. **Operational check:** V3 (done) and V4 (planned).
4. **Exact certificates:** every claimed counterexample or instance ships as a small data file (marker list) plus a verifier independent of the search code.
5. **Reproducibility package:** the `blueprint/verify/` directory, one-command `run_all.sh`, deterministic seeds, and pure Python with no dependencies. For submission: a Zenodo/GitHub release plus optional SageMath cross-check notebooks (factorizations, orders, minimum distances).
6. **Independent re-computation by a second system (planned):** recompute ord(f), the factorizations, and N_f(L) for all tables in SageMath or Magma [O: software availability].

---

## 12. Benchmark strategy

**Allowed benchmark sources.** Only values stated in, or computed from formulas stated in, peer-reviewed indexed publications from the corpus:
- PRA [P2, P3];
- IEEE TQE [P4] (arXiv v2 used; published version [O]);
- Cryptogr. Commun. [P9, P10];
- JAMC [P11];
- IJTP [P8];
- IEEE Access [P6];
- Comput. Appl. Math. [P12];
- ITW proceedings [P7].

No benchmark value is invented. Where a source gives a formula but no number for our instance, the entry is labelled "formula-derived", as with the T–N value 2^{κ−L}.

**Comparisons (all at identical quantum parameters n, k, d_C, d_D, same measured operators):**
1. Number of marker messages at fixed d_sync = L: FTW (1) versus T–N (2^{κ−L}, L ≤ κ) versus ours N_f(L) versus the upper bound ⌊(q^κ − 1)/L⌋.
2. Largest d_sync for a required payload of y bits: T–N (κ − y) versus the exact maximum window of the T–N family itself (computed) versus ours L*(y) = max{L : N_f(L) ≥ 2^y}.
3. Additive (stabilizer) markers: T–N versus best affine versus optimal non-affine.
4. T–N additive sum r + m + d_sync versus 2κ.
5. q-ary families [P9–P11]: first-ever hybrid payloads (no prior benchmark exists, so we report capacity only).

**Fairness notes.**
- For y = 0 the gain κ → ord(f) is FTW's, not ours. Tables mark this column as "[P3]".
- The T–N family's *actual* maximal window often exceeds their Lemma 3 guarantee. For example BCH31-b with y = 1 gives 12 rather than 4, and BCH63-a with y = 1 gives 25 rather than 5 [C]. We report both, so the gain is not over-claimed.
- In BCH31-c for y ≤ 3, the T–N family already reaches 31. Our gains there are at y ≥ 4 (6 → 31 at y = 4, 5 → 31 at y = 5).

---

## 13. Expected tables and figures

Existing computed versions are in `results/tables.md` and the other results files.

- **Table 1** — Literature matrix (§3).
- **Table 2** — Benchmark instances: C, D, κ, ord(f), orbit census [C: T1]. Excerpt:

  | inst. | C ⊂ D | κ | ord f | census |
  |---|---|---|---|---|
  | BCH31-b | [31,16,7] ⊂ [31,21,5] | 5 | 31 | 1 × 31 |
  | BCH31-c | [31,16,7] ⊂ [31,26,3] | 10 | 31 | 33 × 31 |
  | BCH63-b | [63,45,7] ⊂ [63,57,3] | 12 | 63 | 3 × 21, 64 × 63 |
  | BCH63-c | [63,42,7] ⊂ [63,51,5] | 9 | 63 | 1 × 7, 8 × 63 |
  | BCH127-b | [127,99,d_C = OPEN] ⊂ [127,113,5] | 14 | 127 | 129 × 127 |

- **Table 3** — N_f(L) vs FTW vs T–N vs UB [C: T2]. Selected rows (T–N values formula-derived):

  | inst. | L | FTW | T–N | **N_f(L)** | UB |
  |---|---|---|---|---|---|
  | BCH31-b | 2 / 3 / 5 | 1 | 8 / 4 / 1 | **15 / 10 / 6** | 15 / 10 / 6 |
  | BCH31-c | 5 / 10 / 31 | 1 | 32 / 1 / 0 | **198 / 99 / 33** | 204 / 102 / 33 |
  | BCH63-b | 2 / 12 / 63 | 1 | 1024 / 1 / 0 | **2014 / 323 / 64** | 2047 / 341 / 65 |
  | BCH127-b | 5 / 14 / 127 | 1 | 512 / 1 / 0 | **3225 / 1161 / 129** | 3276 / 1170 / 129 |

- **Table 4** — L*(y) vs T–N κ − y [C: T3]. For example, BCH63-b at y = 6 gives 6 vs **63**, and BCH127-b at y = 6 gives 8 vs **127**.
- **Table 5** — Affine y_aff(L) vs ⌊log2 N_f(L)⌋ vs T–N [C: `affine.txt`]. For example, BCH63-a at L = 2…6 gives y_aff = 4, 3, 3, 3, 2, versus log2 N = 4.95, 4.39, 3.91, 3.58, 3.32, versus T–N 4, 3, 2, 1, 0.
- **Table 6** — q-ary instances [C: T4].

  | source | n | q | ord f | N(2) | N(5) | N(ord f) |
  |---|---|---|---|---|---|---|
  | Wang–Zhou | 124 | 5 | 124 | 62 | 24 | 1 |
  | Liu–Kai | 80 | 9 | 80 | 3280 | 1312 | 81 |
  | Shi–Yue–Huang (Remark R) | 35 | 29 | 7 | 12 | 4 | 4 |

- **Table 7** — Simulation results: V3 (done, 100% at ≤ t_D) and V4 (planned).
- **Figure 1** — Schematic of the T-cycles on R_f with packed L-arcs (optimal marker set), next to the T–N affine set.
- **Figure 2** — Frontier log2 N_f(L) vs L for BCH63-b and BCH127-b. Overlays: the T–N line y = κ − L, the bound log2((2^κ − 1)/L), and FTW's point (ord f, 0).
- **Figure 3** — The near-invariant log2 N_f(L) + log2 L ≈ κ across instances (Theorem C). Computed: it lies in [κ − 0.5, κ] for all tabulated L (T2 last column).
- **Figure 4** — Beyond-radius behaviour (planned). Probability of undetected wrong (u, θ) when t_D + 1 bit flips occur, for M = {1} (FTW) vs optimal M. This quantifies the honest cost of dense marker sets.

---

## 14. Parameter / experiment plan

| Block | Parameters | Quantity | Method | Status |
|---|---|---|---|---|
| E1 binary BCH | n ∈ {15, 31, 63, 127}. Dual-containing pairs per FTW Thm 12/13/17 | T1–T3, all L ∈ [2, ord f] | V1, V7 | [C] |
| E1' | n = 255 (κ ≤ 24) | same | V1(d) + C brute force | planned |
| E2 QR | Mersenne primes p ∈ {7, 31, 127} with z deleted factors (XYF Thm 4.5). Other p ≡ −1 (mod 8) (23, 47, 71, 79, 103) evaluated via the general ord(f) criterion | same | V1 | p = 31 [C]; others planned |
| E3 q-ary | P9, P10, P11 examples; P8 examples | N_f(L), max L | V1(d) | 3 instances [C]; P8 planned |
| E4 repeated root | P6 (λ(u+v)\|u−v), P12 (QC) | N_f(L) via divisor form | V1(b) | planned. For P12 the quasi-cyclic shift structure must first be checked to match Lemma 2 [O] |
| E5 optimality | all f of degree ≤ 6 over F_2 and ≤ 3 over F_3 | MIS = N_f(L) | V2 | subset [C]; complete sweep planned |
| E6 decoder | all (instance, L) in Table 3 | success rate, 10^5 trials | V3 | 3000 trials [C]; scale-up planned |
| E7 stabilizer | n = 31 instances; p ∈ {10^−3, …, 10^−1} | logical and message error vs FTW | V4 (stim) | planned [O] |
| E8 affine | κ ≤ 8 exhaustive; larger κ heuristic | y_aff(L) | V5 | κ ≤ 6 [C] |
| E9 beyond radius | t_D + 1, t_D + 2 flips | undetected (u, θ) error | V3 variant | planned |

---

## 15. Risks, failure conditions, and fallback

| Risk | Failure condition | Detection | Fallback |
|---|---|---|---|
| R1 Prior art on multi-marker counting | The coset-code QSC letter (ResearchGate snippet, authors and journal unknown) or classical synchronizable coset-code work (Bose–Caldwell 1967, cited in P8) already gives N_f(L) or the multiplicative trade-off | Obtain and read (§18) before drafting | Reposition: the capacity count becomes a (cited) combinatorial lemma. The contribution becomes the quantum hybrid lift (Thm B), the Z-basis converse (A-iv), the T–N conjecture resolution (Thm C), and the q-ary/repeated-root evaluation |
| R2 T–N published version differs | The TQE version adds larger marker sets, revises the conjecture, or adds the n = 31 BCH section with other numbers | Obtain TQE 7, 2100730 | Re-benchmark against the published statement. Keep Theorem A as the exact optimum |
| R3 "Too elementary" critique | Referees view Thm A as a simple counting argument | — | Emphasize the converse, the tight multiplicative trade-off, Prop. C2, the additive-capacity problem (C-iv), q-ary families, and the decoder (Thm D). Optionally strengthen A-iv to general measurements |
| R4 General-decoder converse fails or is unprovable | Only Z-basis decoders are covered | proof attempt | State the theorem for the class of syndrome/Z-basis decoders, which contains all decoders in the literature. Keep the general case as an open problem |
| R5 Theorem B bookkeeping | Padding or index errors with non-affine markers | V4 stabilizer simulation | Non-affine Q_M is a union of stabilizer-code translates (NK framework [P5]). If T–N Thm 7 cannot be applied directly, prove the synchronization step per inner code, which is always possible since each inner code is a stabilizer code |
| R6 Remark R wrong | Our reading of [P9] Table 4 is mistaken | Re-derive from P9's definitions | Drop Remark R entirely (it is not part of the contribution) |
| R7 Beyond-radius penalty | Dense marker sets raise undetected-error probability beyond t_D | E9 | Report it honestly as a design trade-off. Offer "sparse" admissible sets (sub-maximal M), which the theory also covers |
| R8 q-ary quantum part | Qudit hybrid formalism not verified | — | Restrict Thm B to q = 2. Keep q-ary results at the capacity level (Thm A), which is fully proven and computed |

---

## 16. Paper section-by-section structure

1. **Introduction.** Block synchronization in quantum communication [P2]. QSC families [P3, P6–P12]. Hybrid codes [P4, P5]. The unanswered capacity question. Contributions (Thms A–D). Summary of the numerical gains (Table 3 excerpt).
2. **Preliminaries.** Cyclic codes, order of polynomials, cyclotomic cosets. CSS and dual-containing codes. QSCs in the stabilizer formalism (T–N §3). Hybrid codes (NK definitions).
3. **Marker-hybrid QSCs.** Lemma 1 (D/C ≅ R_f), Lemma 2 (window syndrome), definition of admissibility and capacity.
4. **Exact marker capacity (Theorem A).** Orbit packing, orbit census, divisor and cyclotomic forms, the converse, Corollaries A1–A4.
5. **Optimal synchronizable hybrid codes (Theorem B).** Construction, distance, synchronization and error correction, compatibility with T–N Q3/Q4/Q6, quantum-resource statement.
6. **The synchronization–information trade-off (Theorem C).** Multiplicative bound, tightness, Prop. C2, and the T–N conjecture including the stabilizer-code certificate. Additive capacity as an open problem.
7. **Encoding and decoding (Theorem D).** Irreducible f, the general f table decoder, complexity.
8. **Families and tables.** Binary BCH, QR, Mersenne. q-ary [P9–P11]. Repeated-root [P6] (if E4 is completed).
9. **Numerical validation.** V1–V4, beyond-radius behaviour.
10. **Discussion.** Relation to classical synchronizable codes, limitations (decoder class, q-ary quantum part), open problems (general converse, y_aff, ranking for general f).
- **Appendices.** Full proofs, padding bookkeeping, certificate data, code description.

---

## 17. Required software and code

| Item | Status | Use |
|---|---|---|
| Python ≥ 3.8, standard library only | available; `blueprint/verify/` implemented | V1–V3, V5–V7 |
| `run_all.sh` | implemented (~20 s) | full regeneration of `results/` |
| SageMath or Magma | **not available here [O]** | independent cross-check of factorizations, orders, minimum distances (including d_C of BCH127-b) |
| stim (Clifford simulator) | **not installed [O]** (pip-installable) | V4 stabilizer-level simulation |
| C/NumPy brute-force census | planned | E1' (n = 255, κ up to 24) |
| LaTeX / TikZ / matplotlib | for the paper | figures 1–4 |

---

## 18. Required additional papers and files

Items marked **[O]** are not in the workspace and must be obtained before submission. None of their content is assumed.

1. **Tansuwannont & Nemec, "Synchronizable Hybrid Subsystem Codes," IEEE Trans. Quantum Eng. 7, 2100730 (2026)**: published version [O]. A snippet indicates an added BCH n = 31 example section ([31,26,3], [31,21,5], [31,16,7]). It is needed for the final benchmark and the conjecture wording.
2. **"A New Class of Quantum Synchronizable Codes Derived From Coset Codes"** (letter; authors and venue unknown from the snippet) [O]. Critical overlap check (R1).
3. **Bose & Caldwell, "Synchronizable error-correcting codes," Inf. Control 10(6):616–630 (1967)** (as cited in P8) [O]. Also the classical literature on cyclically permutable and synchronizable coset codes, to be searched; no titles are asserted here. Overlap check (R1).
4. **Grassl, Lu, Zeng, "Codes for Simultaneous Transmission of Quantum and Classical Information," ISIT 2017, pp. 1718–1722** (cited as [17] in P5) [O]. Hybrid-code background.
5. **Ketkar, Klappenecker, Kumar, Sarvepalli, "Nonbinary Stabilizer Codes Over Finite Fields," IEEE TIT 52(11):4892–4914 (2006)** (cited as [18] in P5) [O]. Needed for Thm B-v.
6. **Kremsky, Hsieh, Brun, "Classical enhancement of quantum-error-correcting codes," PRA 78, 012341 (2008)** (cited as [23] in P5) [O]. Related prior work on classical payloads in QECC, for positioning.
7. **Lidl & Niederreiter, *Finite Fields*** (order of polynomials, Thm 3.8; cited as ref. [12] in P3) [O]. Standard reference for §6.
8. A standard reference for Pohlig–Hellman discrete logarithms [O] (Thm D).
9. Repeated-root QSC papers of Luo, Ma and coauthors (IEEE TIT 2018; QIP 2019, as referenced by P6 and P12) [O]. For E4. Exact bibliographic data to be copied from P6/P12's reference lists.
10. Fujiwara–Vandendriessche (IEEE TIT 2014) and Aly–Klappenecker–Sarvepalli (2007, dual-containing BCH), as referenced within the corpus [O]. Exact data to be copied from the citing papers.
11. Further q-ary QSC family papers found by web search (for example IEEE Access "A New Family of QSCs"; arXiv 2110.13659 on length-2^n QSCs) [O]. For extra q-ary benchmark instances only.

---

## 19. References to source papers (corpus: `Quantum Synchronizable.zip`)

- **[P1]** G. G. La Guardia, "New families of asymmetric quantum BCH codes," *Quantum Inf. Comput.* 11(3&4):239–252, 2011.
- **[P2]** Y. Fujiwara, "Block synchronization for quantum information," *Phys. Rev. A* 87, 022344, 2013 (arXiv:1206.0260v5).
- **[P3]** Y. Fujiwara, V. D. Tonchev, T. W. H. Wong, "Algebraic techniques in designing quantum synchronizable codes," *Phys. Rev. A* 88, 012318, 2013.
- **[P4]** T. Tansuwannont, A. Nemec, "Synchronizable hybrid subsystem codes," arXiv:2409.11312v2. Published in *IEEE Trans. Quantum Eng.* 7, 2100730, 2026 (published version not read, [O]).
- **[P5]** A. Nemec, A. Klappenecker, "Infinite families of quantum-classical hybrid codes," arXiv:1911.12260v2, 2020 (journal version to be confirmed [O]).
- **[P6]** C. Du, Z. Ma, L. Luo, D. Huang, H. Wang, "On a family of quantum synchronizable codes based on the (λ(u+v)|u−v) construction," *IEEE Access* 8:8449–8458, 2020 (DOI 10.1109/ACCESS.2019.2963289).
- **[P7]** Y. Xie, J. Yuan, Y. Fujiwara, "Quantum synchronizable codes from augmentation of cyclic codes," *Proc. IEEE Information Theory Workshop (ITW)*, 2014. Page data to be copied from the proceedings.
- **[P8]** Z. Li, S. Zhu, "Two classes of quantum synchronizable codes," *Int. J. Theor. Phys.* 61:251, 2022 (DOI 10.1007/s10773-022-05163-1).
- **[P9]** X. Shi, Q. Yue, X. Huang, "Quantum synchronizable codes from the Whiteman's generalized cyclotomy," *Cryptogr. Commun.* 13:727–739, 2021 (DOI 10.1007/s12095-021-00501-2).
- **[P10]** X. Wang, J. Zhou, "BCH codes with explicit minimum distance and applications in quantum synchronizable codes," *Cryptogr. Commun.* 17:1427–1443, 2025 (DOI 10.1007/s12095-025-00815-5).
- **[P11]** T. Liu, X. Kai, "Some quantum synchronizable codes with explicit distance," *J. Appl. Math. Comput.* 69:1751–1764, 2023 (DOI 10.1007/s12190-022-01811-1).
- **[P12]** C. Du, Z. Ma, Y. Liu, "Quantum synchronizable codes from repeated-root quasi-cyclic codes," *Comput. Appl. Math.* 42:161, 2023 (DOI 10.1007/s40314-023-02298-7).

*(Titles, authors, volumes and pages above were copied from the PDF front matter and running headers.)*

---

## Appendix: Internal novelty and feasibility audit (performed before finalizing)

| Candidate direction | Different from sources? | Provable / computable? | Validation feasible? | Anything invented? | Scope OK? | Decision |
|---|---|---|---|---|---|---|
| New QSC families from yet another cyclic-code class | Weak: the corpus is saturated with this [P6–P12] | yes | yes | no | yes | **Rejected**: incremental |
| Exact minimum distances of QSC ingredient codes | Overlaps [P10, P11] | partly | yes | no | yes | **Rejected**: overlap |
| Fault-tolerant / circuit-level QSC thresholds | new | hard | not within scope (no hardware or noise data) | risk | too big | **Rejected** |
| Qudit version of T–N | light extension | yes | partly | no | yes | **Rejected** as a main topic; kept as B-v [O] |
| Only "use ord(f) instead of κ in T–N" | thin (the M = {1} case of FTW + T–N) | yes | yes | no | too small | **Absorbed** as C-iii(a) |
| **Exact marker capacity plus optimal synchronizable hybrid codes plus trade-off** | yes: new extremal quantity; refutes the T–N conjecture | Theorem A proved (sketch complete); B and D have clear strategies; C2 proved | yes: 4 independent computations, exact MIS, simulation; stabilizer simulation planned | no: all benchmark numbers are formula-derived from cited sources or computed here | one central result | **Selected** |

Remaining honesty flags:
- (i) The converse is proven only for Z-basis (syndrome-type) decoders.
- (ii) The q-ary quantum statement (B-v) is open.
- (iii) Overlap checks R1/R2 depend on documents not yet obtained (§18, items 1–3).
- (iv) Remark R (P9) is unconfirmed and is kept out of the contribution.
