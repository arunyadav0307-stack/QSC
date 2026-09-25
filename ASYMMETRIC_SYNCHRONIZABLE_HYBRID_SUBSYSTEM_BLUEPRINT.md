# Research blueprint: asymmetric synchronizable hybrid-subsystem CSS codes

**Repository:** `arunyadav0307-stack/QSC`
**Branch:** `arena/01a0d961-qsc`
**Blueprint date:** 2026-09-25 (UTC)
**Evidence status:** research hypothesis and implementation plan. No new theorem, parameter set, novelty claim, or computational result is asserted in this document.

## Scope and evidence discipline

This blueprint was prepared after reading all 12 PDFs in `Quantum Synchronizable.zip`, with priority given to the 2024 synchronizable hybrid-subsystem paper, the 2025 explicit-distance BCH paper, and the 2023 quasi-cyclic paper. The repository contains no implementation, benchmark dataset, or author-supplied computational artifact. The temporary extracted text used during review is outside the repository and is not a deliverable.

The central proposal is deliberately narrower than “all asymmetric QSCs” and deliberately stronger than a notation change:

> **Replace the single cyclic chain \(\mathcal C^{\perp}\subset\mathcal C\subset\mathcal D\) by independently designed X- and Z-sector cyclic pairs, then derive—not assume—the fixed marker-check space, symplectic ranks, and shift/label injectivity after gauge fixing.**

The intended primary object is an **asymmetric synchronizable hybrid-subsystem CSS code**, but the original four-code package has failed the first mathematical audit. The corrected direction therefore treats the tuple, the final fixed-check space, and the nuisance-label set as one object. A synchronizable asymmetric CSS/subsystem core is the mandatory first milestone; the hybrid-subsystem lift is not to be claimed unless its rank, gauge-fixing, distance, and marker proof pass the gates in Sections H, I, L, and P.

The notation below distinguishes:

* **Inherited:** already proved or constructed in the cited source papers.
* **Extended:** a direct but nontrivial generalization that still requires a proof in this project.
* **New:** a proposed theorem, family, algorithmic comparison, or empirical result that must not be described as established before completion.

---

## Decisive gate audit (2026-09-25; not a FINAL decision)

This audit is recorded before any manuscript, abstract, or novelty statement is written. The ZIP remains intact and was verified with `unzip -t`. The blueprint is **not FINAL**: the original Gate 1 and Gate 2 formulations fail, and Gate 3 is only provisionally closed for the sources that were accessible. The corrected construction below is the minimum change that keeps the central question mathematically meaningful.

### Gate 1 — static four-code validity

**Result: FAIL for the original package; corrected package adopted.**

For binary subspaces, the source's inner CSS-subsystem notation is

\[
 G_C=\langle X(C_Z^\perp),Z(C_X^\perp)\rangle,
 \qquad
 S_C=\langle X(C_X\cap C_Z^\perp),Z(C_Z\cap C_X^\perp)\rangle .
\]

With

\[
 r_X=\dim(C_X+C_Z^\perp),\qquad
 r_Z=\dim(C_Z+C_X^\perp),
\]
\[
 k=r_X+\dim C_Z-n=r_Z+\dim C_X-n,
 \qquad
 r=r_X-\dim C_X=r_Z-\dim C_Z,
\]

imposing the former package's mandatory \(C_Z^\perp\subseteq C_X\) gives \(r_X=\dim C_X\), hence \(r=0\). It is therefore incompatible with a nontrivial inner gauge sector under this rank framework. The former package also omitted the source disjointness conditions

\[
 (D_X\setminus C_X)\cap C_Z^\perp=\varnothing,
 \qquad
 (D_Z\setminus C_Z)\cap C_X^\perp=\varnothing .
\]

The corrected candidate package is instead

\[
 C_X\subseteq D_X,\qquad C_Z\subseteq D_Z,
\]
\[
 (D_X\setminus C_X)\cap C_Z^\perp=\varnothing,
 \qquad
 (D_Z\setminus C_Z)\cap C_X^\perp=\varnothing,
\tag{G1-static}
\]

plus whichever outer CSS commutation condition is required by the selected decoder (for example \(D_Z^\perp\subseteq D_X\)) and a post-gauge-fixing symplectic rank test. The cross-dual inclusion \(C_Z^\perp\subseteq C_X\) is retained only as a deliberately labeled stabilizer-limit specialization, not as a mandatory inner condition. Conditions (G1-static) are necessary candidate conditions, not yet a sufficient theorem.

### Gate 2 — actual marker syndrome

**Result: FAIL for the original quotient-only formulation; corrected formulation adopted.**

Let \(F_X\) be the row space of the fixed Z-type marker checks, let \(E_X=F_X^\perp\), let \(b_X\in D_X\setminus C_X\) be a marker, and let \(u\) be the total X-type nuisance component from a permitted gauge or classical-label representative. The measured object is the actual syndrome

\[
 \sigma_{\alpha,u}=H_{F_X}O(b_X+u,-\alpha)^T .
\tag{G2-syndrome}
\]

If \(F_X=C_X^\perp\), \(b_X=g_{D_X}\), and every allowed nuisance component lies in \(C_X\), then and only then the usual quotient reduction is justified:

\[
 f_X=g_{C_X}/g_{D_X},
 \qquad
 \sigma_{\alpha,u}\longleftrightarrow x^{-\alpha}\pmod {f_X} .
\tag{G2-pure}
\]

If the nuisance vector is in \(D_X\) but not in \(C_X\), the correct residue is instead

\[
 x^{-\alpha}\left(1+\frac{u(x)}{g_{D_X}(x)}\right)\pmod {f_X(x)},
\tag{G2-joint}
\]

up to the chosen sign convention for cyclic shifts. If it is not in \(D_X\), there is no valid division by \(g_{D_X}\); the direct matrix syndrome must be used.

For a shift-invariant check space, the exact general marker polynomial is defined by the cyclic ideal

\[
 I(F_X,b_X)=\{p(x)\in R_n:p(x)b_X(x)\in E_X\},
 \qquad
 I(F_X,b_X)=\langle\phi_{F_X,b_X}(x)\rangle .
\]

The shift period is \(\operatorname{ord}(\phi_{F_X,b_X})\), when the order is defined in the usual divisor sense. In the full-check special case \(F_X=C_X^\perp\), \(E_X=C_X\), and \(b_X=g_{D_X}\), this generator is \(f_X\). For a non-cyclic check space, no polynomial shortcut is permitted: injectivity is the finite matrix condition on (G2-syndrome).

Thus the proof target is either a pure-marker theorem with all gauge/label X components inside \(C_X\), or a joint injectivity theorem over allowed \((\alpha,u)\) pairs. The quotient alone is not a marker theorem.

### Gate 3 — exact prior-work intersection

**Result: provisionally PASS for the accessible scholarly search, but FAIL-CLOSED for a final novelty claim.**

The accessible search found: (i) asymmetric cyclic/subsystem work without synchronization, (ii) synchronizable QSC work without independent X/Z hybrid-subsystem markers, and (iii) the 2024/2026 common-pair synchronizable hybrid-subsystem source, whose general CSS section contains four classical spaces but whose synchronization construction does not prove the independent four-code marker statement targeted here. No clearly identical published result was located. This is a qualified gap observation, not an absence theorem.

The exact query log and matrix are in Sections O, S, and V. Direct Web of Science, Scopus, MathSciNet, and some IEEE Xplore query pages were not fully accessible in this environment; their records remain **OPEN**. Until those searches and the final IEEE TQE version are archived, the document must say “no exact match identified in the searched/accessed sources,” never “first” or make an absolute novelty claim.

### Current decision

The direction is retained **provisionally**, with the original package and quotient claim removed. The project is **NO-GO for FINAL or for a novelty claim** until the corrected Gate 1 and Gate 2 proofs/obstructions, at least one nontrivial rank profile, and the outstanding Gate 3 search records are closed.

# Source audit before the proposed work

## Repository inventory and provenance

| Local PDF | Paper or source | Mathematical role in this blueprint |
|---|---|---|
| `1206.0260v5.pdf` | Y. Fujiwara, **Block synchronization for quantum information**, *Physical Review A* 87, 022344 (2013), arXiv v5 | Original QSC encoding/decoding framework and CSS/cyclic chain construction. |
| `Algebraic techniques in designing quantum synchronizable codes.pdf` | Y. Fujiwara, V. Tonchev, T. Wong, **Algebraic techniques in designing quantum synchronizable codes**, *Physical Review A* 88, 012318 (2013), DOI 10.1103/PhysRevA.88.012318 | Polynomial-order refinement; the order of the quotient polynomial, rather than merely its degree, controls synchronization. |
| `Quantum_Synchronizable_Codes_From_Augmen.pdf` | Y. Xie, J. Yuan, Y. Fujiwara, **Quantum synchronizable codes from quadratic residue codes and their supercodes**, source archive PDF | Binary quadratic-residue and augmented-code family attaining the length upper bound in selected prime-length cases. |
| `0239-0252.pdf` | G. G. La Guardia, **New families of asymmetric quantum BCH codes**, *Quantum Information and Computation* 11(3–4), 239–252 (2011) | Independent asymmetric CSS/BCH construction; supplies the X/Z separation that QSC papers in the archive do not use in their main chain. |
| `1911.12260v2.pdf` | A. Nemec, A. Klappenecker, **Infinite Families of Quantum-Classical Hybrid Codes**, arXiv:1911.12260v2 (2020) | Hybrid-code definitions, detectable-error condition, hybrid weight-enumerator and parameter-comparison context. |
| `On_a_Family_of_Quantum_Synchronizable_Codes_Based_on_the_lambdau__vu_-_v_Construction.pdf` | C. Du, Z. Ma, L. Luo, D. Huang, H. Wang, **On a Family of Quantum Synchronizable Codes Based on the \((\lambda(u+v)\mid u-v)\) Construction**, *IEEE Access* (2020), DOI 10.1109/ACCESS.2019.2963289 | Nonbinary, repeated-root, cyclic/constacyclic and maximum-order QSC construction; a possible but intentionally out-of-scope alternative family. |
| `s12095-021-00501-2.pdf` | X. Shi, Q. Yue, X. Huang, **Quantum synchronizable codes from the Whiteman’s generalized cyclotomy**, *Cryptography and Communications* 13, 727–739 (2021), DOI 10.1007/s12095-021-00501-2 | Maximum-order factor selection from \(\Phi_{p_1p_2}(x)\); published cyclic benchmarks. |
| `s10773-022-05163-1.pdf` | Z. Li, S. Zhu, **Two Classes of Quantum Synchronizable Codes**, *International Journal of Theoretical Physics* 61, 251 (2022), DOI 10.1007/s10773-022-05163-1 | Odd-prime cyclic/negacyclic and BCH/negacyclic-BCH constructions; maximum attainable synchronization under stated residue conditions. |
| `s12190-022-01811-1.pdf` | T. Liu, X. Kai, **Some quantum synchronizable codes with explicit distance**, *Journal of Applied Mathematics and Computing* 69, 1751–1764 (2023), DOI 10.1007/s12190-022-01811-1 | Three BCH families with explicit classical distances and maximum-order QSCs; important reproducible baselines. |
| `s40314-023-02298-7.pdf` | C. Du, Z. Ma, Y. Liu, **Quantum synchronizable codes from repeated-root quasi-cyclic codes**, *Computational and Applied Mathematics* 42, 161 (2023), DOI 10.1007/s40314-023-02298-7 | First archive source that extends QSCs beyond ordinary cyclic codes; provides QC containment/order tests and sample tables. |
| `2409.11312v2.pdf` | T. Tansuwannont, A. Nemec, **Synchronizable hybrid subsystem codes**, arXiv:2409.11312v2 (25 Sep 2024) | Most important foundation for the proposed hybrid-subsystem extension. The arXiv record now lists an IEEE Transactions on Quantum Engineering 2026 journal version, DOI 10.1109/TQE.2026.3673092; the publisher version is not in the repository and must be diffed before publication work. |
| `s12095-025-00815-5.pdf` | X. Wang, J. Zhou, **BCH codes with explicit minimum distance and applications in quantum synchronizable codes**, *Cryptography and Communications* 17, 1427–1443 (2025), DOI 10.1007/s12095-025-00815-5 | Most recent local QSC construction source; explicit-distance lemmas, length lifting, exact-order argument, Magma-checked examples and comparison tables. |

## Findings from each relevant source

### 1. Fujiwara 2013: the inherited synchronization mechanism

The construction starts with a dual-containing cyclic code \(C\) of length \(n\), dimension \(k_1\), and a containing cyclic code \(D\) of dimension \(k_2>k_1\). If \(g_1(x)\) and \(g_2(x)\) are their generator polynomials and \(f(x)=g_1(x)/g_2(x)\), the source construction supports an \((a_l,a_r)\)-QSC with

\[
 a_l+a_r<\operatorname{ord}(f),\qquad
 [[n+a_l+a_r,\,2k_1-n]],
\]

correcting phase errors according to the inner code and bit errors according to the containing code. The encoding attaches ancillas and uses CNOTs to copy boundary portions of a shifted cyclic codeword. The receiver first corrects bit errors on an \(n\)-qubit window, extracts a synchronization syndrome, realigns, and then performs the remaining CSS corrections.

The crucial assumption is code-capacity noise: the source treats Pauli errors on data qubits and does not provide a fault-tolerant syndrome-extraction construction. The original presentation is a common-chain/symmetric CSS construction; it does not independently select X- and Z-sector classical codes.

### 2. Fujiwara–Tonchev–Wong 2013: order, not degree

The paper proves that the number of distinguishable shifts is controlled by the polynomial order \(\operatorname{ord}(f)\), with \(\operatorname{ord}(f)\) the least positive \(e\) such that \(f(x)\mid x^e-1\). For pairwise coprime irreducible factors, the order is the least common multiple of their orders. A primitive factor can force order \(n\), giving the maximum allowable total misalignment \(a_l+a_r<n\). The paper supplies constructions from BCH and punctured Reed–Muller families and explains why the older degree-only bound is weaker.

Its primitive BCH specialization gives a useful regression test: for suitable binary primitive lengths and two odd designed distances, the quotient contains factors whose combined order is the length. The paper also notes repeated-root complications and discusses deletion/loss as distinct from ordinary misalignment.

### 3. Quadratic-residue augmentation

The quadratic-residue paper uses binary QR codes and their augmented supercodes at prime lengths, especially Mersenne-prime lengths. The quotient can have order equal to the prime length, reaching the synchronization upper bound. The distance and dimension behavior of augmented QR codes is less uniformly explicit than the later BCH work. This is a benchmark family, not the proposed construction family.

### 4. La Guardia 2011: the asymmetric CSS precedent

This source explicitly constructs nonbinary asymmetric quantum BCH codes using two different classical code roles. It defines separate X-/qudit-flip and Z-/phase-shift distances and proves parameter families such as

\[
[[n,\,n-m(4q-c-5)-2,\,d_z\ge 2q+2\,/\,d_x\ge 2q-c]]_q
\]

under its stated primitive BCH assumptions. The source also gives the CSS distance expressions as coset distances, not merely raw classical minimum distances. It does **not** address block synchronization, cyclic-marker syndromes, gauge fixing, or hybrid-subsystem structure. This is the principal source establishing that independent X/Z classical design is mathematically natural rather than cosmetic.

### 5. Nemec–Klappenecker 2020: hybrid-code context

The paper defines an \(((n,K:M))_q\) hybrid code as a direct sum of \(M\) orthogonal \(K\)-dimensional quantum codes and gives the hybrid Knill–Laflamme detectable-error condition. It derives hybrid weight enumerators and linear-programming bounds and constructs infinite families of small-distance hybrid stabilizer codes. It is not a QSC paper and does not supply a synchronization marker. Its role is to prevent misuse of the word “hybrid”: a future code must explicitly identify the classical sectors and their detectable-error condition.

### 6. The \((\lambda(u+v)\mid u-v)\) construction

The 2020 *IEEE Access* paper builds QSCs from repeated-root cyclic and constacyclic components through the \((\lambda(u+v)\mid u-v)\) map. It proves divisibility/dual-containment conditions and obtains maximum synchronization order in several cases, with examples comparing bit-error performance against projective-geometry QSCs. The construction is nonbinary and algebraically heavier than needed for the first asymmetric hybrid-subsystem test. It is retained as a secondary benchmark and a possible later generalization, not mixed into the central experiment.

### 7. Whiteman generalized cyclotomy

The 2021 paper factors \(\Phi_{p_1p_2}(x)\), uses reciprocal/nonreciprocal factors to establish dual containment, and selects a quotient factor of \(\Phi_n(x)\) so that its order is \(n=p_1p_2\). It gives explicit lower bounds and Magma-checked examples; for example, at \(q=29,n=35\), it reports dual-containing classical codes with parameters such as \([35,31,3]_{29}\), \([35,30,4]_{29}\), \([35,29,5]_{29}\), and \([35,28,6]_{29}\), and corresponding maximum-order QSCs. These are reputable published benchmarks, but they use one common cyclic chain.

### 8. Two classes of QSCs

The 2022 paper constructs QSCs from odd-prime cyclic and negacyclic codes and from BCH/negacyclic-BCH codes in a \((u+v\mid u-v)\) structure. The stated conditions can attain the best attainable synchronization tolerance. The reported examples include a ternary length-80 construction with dimension 48 and one correctable bit and phase error. The source is useful for checking that a new result is not merely a rephrasing of a ring/negacyclic construction.

### 9. Liu–Kai 2023: explicit-distance cyclic baselines

The paper treats three families:

* \(n=2^a(q-1)\) with \(q\equiv3\pmod4\) and \(2^a\Vert(q+1)\);
* \(n=2^b(q+1)\) with \(q\equiv1\pmod4\) and \(2^b\Vert(q-1)\);
* \(n=q^{2\ell}-1\) with the stated odd-prime-power and BCH conditions.

It proves dual containment, exact distances for the selected cyclic codes, and maximum-order quotients. The recorded examples include the published \(q=7,n=2400\) case with classical parameters \([2400,2352,15]\) and \([2400,2384,5]\), yielding a QSC of dimension 2304 correcting up to 7 phase and 2 bit errors, and the \(q=5,n=624\) case yielding dimension 576 with 3 phase and 1 bit error. These values are source benchmarks only; they are not proposed results.

### 10. Repeated-root quasi-cyclic QSCs

The 2023 QC paper generalizes cyclic QSCs to selected 2-generator quasi-cyclic codes. Its central theorem assumes QC codes \(C\subset D\), \(C^\perp\subset C\), a common nontrivial coordinate gcd, and a polynomial quotient/order condition. The proof obtains the synchronization syndrome from a QC generator block. It then specializes to repeated-root QC codes generated by forms such as \((g(x),k(x)g(x))\), \((0,f(x))\), and \((g(x),k(x)g(x)),(f(x),f(x))\), with sufficient dual-containment and distance bounds. The paper supplies sample parameter tables, including large lengths and small or lower-bounded distances.

This source establishes that “QSC plus a more general classical code” is not by itself new. The present proposal therefore does not claim novelty from using BCH codes, from using QC codes, or from replacing a polynomial ring; the proposed contribution is the asymmetric marker-compatible hybrid-subsystem theorem.

### 11. Wang–Zhou 2025: most recent explicit-distance baseline

The 2025 paper proves an exact-distance lemma for a BCH defining interval when

\[
(\lambda_2-\lambda_1+1)\frac{q^m-1}{q-1}<n,
\]

and lifts an exact-distance code at length \(n_1\) to a code at a multiple length \(n_2\). Its QSC theorem uses two cyclic codes with \(C_1^\perp\subset C_1\subset C_2\), proves exact or explicit classical distances, and obtains order \(n\) when the quotient contains a factor with a primitive \(n\)-th root. It includes examples at \(q=5,n=124\), \(q=17,n=16704\), and a lifted \(q=5,n=372\) case, and states that its parameters were checked with Magma.

This is the preferred source for exact-distance certificates in the proposed small-to-moderate BCH search. The paper still uses a common pair and does not include independent X/Z hybrid-subsystem marker sectors.

### 12. Tansuwannont–Nemec 2024 arXiv / 2026 journal version

The 2024 manuscript is the most important conceptual source. It starts from one binary cyclic chain

\[
\mathcal C^\perp\subset\mathcal C\subset\mathcal D,
\]

with dimensions \(k_c,k_d\), distances \(d_c,d_d\), and quotient order represented in the cyclic marker construction. It derives:

* a common-pair QSC;
* a nonsynchronizable subsystem code with \(2k_c-n\) logical qubits and \(2(k_d-k_c)\) gauge qubits;
* a synchronizable subsystem code with \(k_d-k_c\) gauge qubits;
* a synchronizable hybrid code with \(k_d-k_c\) classical bits;
* a family trading classical bits for synchronization distance; and
* synchronizable and nonsynchronizable hybrid-subsystem variants.

The paper develops flexible hyperbolic generator choices, the shifted syndrome identity involving \(H_C O(q_1,-\alpha)^T\), and general CSS subsystem/hybrid constructions from \(C_x,C_z,D_x,D_z\). Its Corollary 2 gives the resource identities

\[
 r+m+d_{\rm sync,max}=2(k_d-k_c)
\]

for its synchronizable family and one larger value for the nonsynchronizable family, while explicitly presenting optimality as a conjecture rather than a theorem.

Its limitations are decisive for the present design: the main synchronization proof uses one common cyclic pair, the noise model is code capacity only, gate and measurement faults are absent, and the paper leaves other QSC families, qudits, general classical codes, and fault-tolerant procedures open. The current arXiv record lists an IEEE Transactions on Quantum Engineering 2026 version; the repository contains only v2 of the arXiv manuscript, so the journal version must be obtained and compared before citing final theorem numbers.

## Source issues that are not silently repaired

The following source-reading issues are preserved as OPEN rather than normalized into the proposed framework:

1. **Synchronization-distance convention:** the 2024 manuscript uses both the allowance condition \(a_l+a_r<k_d-k_c\) and a synchronization-distance convention that counts the correctly aligned position. The resulting off-by-one distinction between total misalignment allowance and `d_sync` must be checked against the publisher version, DOI 10.1109/TQE.2026.3673092, before quoting a resource identity.
2. **Publisher-version changes:** local `2409.11312v2.pdf` is the arXiv manuscript, not the final IEEE TQE PDF. Final theorem numbers, pagination, and any post-review corrections remain OPEN.
3. **OCR/equation ambiguity:** temporary extraction of several PDFs loses superscripts, reciprocal symbols, and floor signs. The exact BCH, repeated-root, and constacyclic hypotheses must be transcribed from the PDF pages or publisher versions before formal reuse.
4. **QC examples:** the 2023 repeated-root QC PDF contains compressed notation and at least one extracted example whose total-length expression is incomplete in text extraction. No QC numerical value from that extraction will be used as a headline benchmark without a page-level recheck.
5. **Computational artifacts:** the sources mention Magma or online code tables but the repository contains no scripts, raw search logs, or datasets. Any reproduced value will be labeled independently recomputed, not source-computed.

## Candidate-direction feasibility screen

The following three candidates were evaluated internally before selecting one direction. The scores are qualitative planning judgments, not experimental results.

| Candidate | Mathematical novelty | Proof feasibility | Computation/validation | Benchmark availability | Q1-level potential | Decision |
|---|---|---|---|---|---|---|
| Four-code asymmetric synchronizable hybrid-subsystem CSS construction | High if the marker/gauge theorem succeeds; not present in the local source chain | Medium: the marker-compatible gauge step is the main risk but is finite-dimensional and testable | High for binary BCH lengths and small exhaustive checks | High: common-pair QSC, asymmetric CSS/BCH, exact-distance BCH, and hybrid-subsystem sources are available | High if it yields a theorem plus nontrivial certified Pareto points | **Selected provisionally; not FINAL** |
| Repeated-root/quasi-cyclic asymmetric hybrid-subsystem QSC | Medium: the local 2023 QC paper already supplies the basic noncyclic QSC mechanism | Medium-low because QC dual/gauge/order bookkeeping compounds the four-code proof | Medium; source examples exist but distance certificates and decoders are less uniform | Medium | Medium, unless a genuinely new QC theorem emerges | Rejected for this focused project |
| Universal resource-optimality theorem for synchronizable hybrid-subsystem codes | Potentially high | Low: the 2024 source states optimality as a conjecture and the general converse is not identified | Low-to-medium; finite searches cannot establish a universal converse | Medium | Potentially high but unreliable within one executable project | Rejected for now |

The first row is the single selected direction. The other rows are not alternative blueprints; they are rejected feasibility screens.

## Cross-source decision

The following alternatives were considered and rejected as the central direction:

1. **Only another ordinary cyclic QSC family:** already heavily covered by the 2013–2025 sources and not a substantive extension of the latest hybrid-subsystem theorem.
2. **Only a QC/repeated-root QSC:** mathematically useful, but the 2023 source already proves the basic noncyclic-QSC mechanism; a simple transplant would fail the nontrivial novelty test.
3. **A qudit or fault-tolerant construction:** important but requires additional finite-field and circuit-fault infrastructure absent from the repository; reliable validation is not yet feasible within one focused project.
4. **Only a new resource-tradeoff bound:** potentially strong, but the 2024 optimality conjecture is not enough by itself to guarantee an explicit computationally testable code family.

The selected direction combines the strongest recent synchronizable hybrid-subsystem framework with the independent X/Z CSS design problem and exact-distance BCH verification. Its risk is real, but its algebraic conditions and finite-length tests are executable.

---

# A–V research blueprint

## A. Title

**Asymmetric Synchronizable Hybrid-Subsystem CSS Codes from Two Independently Nested Cyclic Pairs**

Working short title: **ASH-CSS**.

The title does not claim that the construction already exists. It names the object to be proved or rejected.

## B. Precise research problem

### Problem statement

A synchronizable CSS code must do two logically different jobs:

1. correct X- and Z-type Pauli errors; and
2. identify a block displacement from a quantum syndrome without measuring the encoded state destructively.

The common-chain construction controls both jobs through one pair \(\mathcal C\subset\mathcal D\). The latest hybrid-subsystem framework adds gauge and classical sectors, but still uses the same cyclic pair for the marker and for both CSS sectors. Standard asymmetric CSS constructions use distinct classical codes for X and Z protection, but do not prove that their syndrome structure survives quantum block misalignment or the hybrid-subsystem gauge operations.

## C. Literature/source gap identified from the provided material

### Gap statement

The repository contains no proved construction that simultaneously has all four properties:

1. separate X/Z classical code choices;
2. a cyclic-order synchronization marker with a uniqueness proof;
3. a hybrid-subsystem gauge/classical sector; and
4. independently computed X- and Z-distance guarantees.

This is an **internal repository gap**, not yet a publication-level absence claim. A full external novelty search is a mandatory gate in Section V.

### Central research question

> **Can four classical cyclic codes \((C_X,C_Z,D_X,D_Z)\), with the two sector-wise nestings \(C_X\subseteq D_X\) and \(C_Z\subseteq D_Z\) plus a marker-compatible gauge-fixing profile, produce a synchronizable hybrid-subsystem CSS code whose shift syndrome is provably injective and whose X/Z distances can be tuned independently?**

The answer may be negative. A negative result caused by an explicit obstruction would still be mathematically useful, but the project must not call a failed construction a new code family.

## D. Source-paper foundation and exactly what is reused

### Inherited without alteration

* Fujiwara’s ancilla/CNOT extension and windowed recovery protocol.
* The polynomial quotient-order criterion \(a_l+a_r<\operatorname{ord}(f)\).
* CSS commutation and asymmetric distance formulas.
* The 2024 paper’s hyperbolic Pauli-generator and gauge-fixing methodology.
* The 2024 shifted-syndrome identity and the distinction between stabilizer, gauge, logical, and classical-label operators.
* Published BCH dual-containment, cyclotomic-coset, order, and explicit-distance lemmas.

### Extended but not yet proved

* Replace the common \(C,D\) pair by X/Z pairs.
* Fix only the marker-relevant gauge sector while preserving nontrivial gauge and classical payloads.
* Prove that the measured marker syndrome remains distinct for all allowed shifts and all allowed classical labels.
* Derive the resulting dressed X/Z distances rather than substituting raw classical distances.

### Genuinely new if successful

* A four-code marker-compatible synchronizable hybrid-subsystem theorem.
* An explicit asymmetric BCH family satisfying the four-code and marker conditions.
* A reproducible rank/order/distance search and a Pareto comparison against the common-pair baselines.
* A nontrivial novelty result showing that the construction is not a relabeling or a source specialization.

## E. Central novel contribution

### Core contribution: a rank-defined, marker-compatible four-code theorem

Let \((C_X,C_Z,D_X,D_Z)\) be binary cyclic codes of length \(n\). The theorem target is **not** the former package (P). It is a theorem, or an explicit obstruction, for tuples satisfying the static conditions (G1-static), an explicitly specified outer commutation condition, and a final symplectic gauge-fixing profile. The inner Pauli group is allowed to be nonabelian:

\[
G_C=\langle X(C_Z^\perp),Z(C_X^\perp)\rangle,
\qquad
S_C=\langle X(C_X\cap C_Z^\perp),Z(C_Z\cap C_X^\perp)\rangle.
\]

The construction must then produce a fixed stabilizer \(S_F\), a gauge group \(G_F\), and a classical-label set \(L_F\) by explicit symplectic reduction. A separate outer CSS condition such as \(D_Z^\perp\subseteq D_X\) may be imposed for the preliminary X-sector decoder, but it does not replace the rank test or the marker test.

The marker target is \(b_X=g_{D_X}\in D_X\setminus C_X\) with full fixed check space \(F_X=C_X^\perp\) only when that space can actually be fixed. The quotient \(f_X=g_{C_X}/g_{D_X}\) is a valid control polynomial only under the nuisance condition in Gate 2. Otherwise the theorem must use \(\phi_{F_X,b_X}\) or the direct joint syndrome map.

### Explicit family component

Use primitive binary BCH defining sets as the first computational family. The code search will choose different X/Z inner and outer roles and will certify, rather than assume, inclusions, disjointness, exact distances, quotient/annihilator order, and the final hybrid-subsystem ranks.

### Reproducible validation component

Produce a public, deterministic implementation that independently checks the polynomial construction, symplectic matrices, fixed-check syndrome table, shift/label injectivity, exact small-code distances, and code-capacity decoding simulations. Computation supports the theorem and parameter claims; it does not replace the proof.

### What is genuinely new only if proved

The proposed new object is the **combination** of independently chosen X/Z cyclic pairs with a rank-derived fixed marker-check space and a joint shift/label injectivity proof. A four-code list, a different BCH interval, or a basis change alone is explicitly not a contribution.

## F. Research questions and hypotheses

### One central question

The central question is the one in Section B. All experiments must serve it.

### Testable hypotheses

* **H1 — pure-marker hypothesis:** if the final fixed marker checks are \(F_X=C_X^\perp\), \(b_X=g_{D_X}\), and every allowed free gauge/label X component lies in \(C_X\), then the actual syndrome is injective on the allowed shift interval whenever
  \[
  a_l+a_r<\operatorname{ord}(f_X).
  \]
* **H1' — joint-marker hypothesis:** without that nuisance containment, the joint map \((\alpha,u)\mapsto H_{F_X}O(b_X+u,-\alpha)^T\) is injective modulo the declared gauge equivalence relation for the allowed shift and label set. No quotient-only claim is made in this case.
* **H2 — asymmetric-distance hypothesis:** changing \(C_Z\) independently of \(C_X\) changes the final dressed Z distance and/or the quantum/classical/gauge ranks without destroying the marker condition.
* **H3 — rate/usefulness hypothesis:** on a fully specified biased code-capacity Pauli channel, at least one certified candidate improves a declared fixed-resource objective relative to the matched common-pair synchronizable hybrid-subsystem baseline. If no point does so, the result is a characterized negative or unresolved direction.
* **H4 — nontriviality hypothesis:** successful points require genuinely distinct X/Z sectors and cannot be transformed into the 2024 common-pair construction by swapping labels, changing a generator basis, or selecting a different hyperbolic basis.

H1–H4 are hypotheses, not results. In particular, the Gate 1 rank obstruction is already known for the discarded cross-dual specialization and is not counted as a new theorem.

## G. Mathematical framework and required definitions

### G.1 Primary field and cyclic ring

The first paper will work over \(\mathbb F_2\) and

\[
R_n=\mathbb F_2[x]/\langle x^n-1\rangle.
\]

The binary restriction is intentional: it makes the symplectic, exhaustive small-length, and shift-syndrome checks independently implementable. A q-ary extension is OPEN and is not part of the acceptance criteria.

A cyclic code is an ideal generated by a divisor \(g(x)\mid x^n-1\). For \(C\subseteq D\), write \(g_D\mid g_C\). The candidate marker is initially \(b_X=g_{D_X}\), and the full-check quotient is

\[
 f_X(x)=\frac{g_{C_X}(x)}{g_{D_X}(x)}.
\]

This quotient is nonconstant only when \(C_X\subsetneq D_X\). Its order is the least positive \(e\) with \(f_X(x)\mid x^e-1\). It is not automatically the order of the actual marker syndrome; the actual check space and nuisance set must first pass Gate 2.

### G.2 Inner CSS-subsystem spaces and rank obstruction

For binary linear codes \(C_X,C_Z\subseteq\mathbb F_2^n\), define

\[
G_C=\langle X(C_Z^\perp),Z(C_X^\perp)\rangle,
\]
\[
S_C=\langle X(C_X\cap C_Z^\perp),Z(C_Z\cap C_X^\perp)\rangle.
\]

The source-compatible rank quantities are

\[
 r_X=\dim(C_X+C_Z^\perp),\qquad
 r_Z=\dim(C_Z+C_X^\perp),
\]
\[
 k=r_X+\dim C_Z-n=r_Z+\dim C_X-n,
 \qquad
 r=r_X-\dim C_X=r_Z-\dim C_Z.
\tag{G-ranks}
\]

The implementation must verify these formulas against the binary symplectic matrices. The former condition \(C_Z^\perp\subseteq C_X\) is a stabilizer-limit condition for this group because it forces \(r=0\); it is not imposed in the nontrivial gauge search.

If a stabilizer-only asymmetric CSS core is needed for a regression, use its own cross-dual condition and label it as the \(r=0\) specialization. Do not call it the general hybrid-subsystem construction.

### G.3 Four-code static package

The corrected candidate package is

\[
 C_X\subseteq D_X,\qquad C_Z\subseteq D_Z,
\]
\[
 (D_X\setminus C_X)\cap C_Z^\perp=\varnothing,
 \qquad
 (D_Z\setminus C_Z)\cap C_X^\perp=\varnothing,
\tag{G-static}
\]

with a separately declared outer condition such as \(D_Z^\perp\subseteq D_X\) when the preliminary outer CSS decoder requires it. Define \(G_D,S_D\) analogously only when the selected source construction calls for them. The tuple is accepted only after the exact symplectic commutation and rank conditions are checked; no inclusion is silently promoted to sufficiency.

The marker candidate is \(b_X\in D_X\setminus C_X\), with \(b_X=g_{D_X}\) used for the cyclic quotient experiment. A non-generator marker is allowed only if its actual syndrome period is computed and certified.

### G.4 Fixed marker checks and the exact nuisance set

Let \(F_X\) be the binary row space of Z-type checks that are fixed in every sector used for synchronization. Let \(E_X=F_X^\perp\), and define the allowed nuisance set \(\mathcal U_X\) to contain the X-vector components of every freely varying gauge representative, classical-label representative, and marker-preserving encoding choice that can occur before the marker syndrome is read. Gauge-equivalent representatives must be quotiented explicitly; they cannot be silently treated as distinct labels.

The actual measurement is

\[
 \sigma_{\alpha,u}=H_{F_X}O(b_X+u,-\alpha)^T,
 \qquad u\in\mathcal U_X.
\tag{G-syndrome}
\]

The simplest profile has \(F_X=C_X^\perp\). It is admissible only if the symplectic gauge-fixing routine can fix these checks while removing or reclassifying their X conjugates. If a proper check space is used, the polynomial \(f_X\) is not substituted for the direct syndrome period.

For a shift-invariant \(F_X\), define

\[
 I(F_X,b_X)=\{p\in R_n:p b_X\in E_X\}=\langle\phi_{F_X,b_X}\rangle.
\tag{G-annihilator}
\]

For \(F_X=C_X^\perp\) and \(b_X=g_{D_X}\), \(\phi_{F_X,b_X}=f_X\) under the standard cyclic representative convention. If \(u\in C_X\), the full-check syndrome reduces to \(x^{-\alpha}\pmod {f_X}\); if \(u\in D_X\setminus C_X\), it is the joint residue in (G2-joint). For non-cyclic \(F_X\), the only accepted period is the direct finite matrix period.

### G.5 Concrete symplectic gauge-fixing profile

Start with the source-derived generator matrices \(S_0,G_0\) and candidate classical-label set \(L_0\) for the tuple. The implementation must not assume that a common-pair hyperbolic basis remains valid.

1. Compute independent bases for the candidate marker space \(W_X=\{Z(v):v\in F_X\}\), the source stabilizer, and all label spaces.
2. Use symplectic Gram–Schmidt on \(G_0\) to identify every X-type conjugate of a proposed fixed marker check.
3. Add only the mutually commuting selected checks to the final fixed stabilizer \(S_F\), and remove or reclassify each conjugate as a gauge or fixed label according to the resulting commutation table.
4. Construct the remaining gauge group \(G_F\) and label set \(L_F\), then compute \(s=\operatorname{rank}S_F\), \(g=\operatorname{rank}G_F\), and the commutator rank of \(G_F\).
5. Reject the profile if \(S_F\) is not isotropic, \(S_F\not\subseteq G_F\), the claimed labels fail to commute with \(S_F\), the commutator rank is inconsistent with the claimed gauge count, or the actual map (G-syndrome) has a shift/label collision.

The profile may reduce \(m\) or \(r\). That reduction is part of the result, not an implementation detail.

### G.6 Hybrid-subsystem parameters

For a clean sector, compute

* \(s=\operatorname{rank}(S_F)\);
* \(g=\operatorname{rank}(G_F)\);
* \(r=(g-s)/2\), only after the gauge commutator rank verifies the subsystem interpretation;
* \(k=n-s-r\); and
* \(m\) by explicitly identifying independent classical-label eigenvalue choices after gauge fixing.

The direct-sum dimension must be checked against \(2^{k+r}2^m\) for the declared sector decomposition. Closed formulas in the four classical dimensions are targets, not inputs.

### G.7 Final dressed distances

For the fixed stabilizer/gauge pair, define the harmful X- and Z-type distances by

\[
 d_X^F=\min\{\operatorname{wt}(u):X(u)\in N(S_F)\setminus G_F\},
\]
\[
 d_Z^F=\min\{\operatorname{wt}(v):Z(v)\in N(S_F)\setminus G_F\}.
\tag{G-distance}
\]

These definitions count a classical-label-changing operator as harmful unless the experiment explicitly declares a different decoding task. The source-inspired expressions involving \(D_X+D_Z^\perp\) and \(D_Z+D_X^\perp\) are retained only as candidate lower-bound formulas to be proved or refuted; they are never headline distances before (G-distance) is evaluated.

## H. Proposed code/construction framework

### H.1 Classical-code selection

1. Choose \(n\) and four binary cyclic defining sets or generator polynomials.
2. Build \(C_X,C_Z,D_X,D_Z\) and verify (G-static), the selected outer commutation condition, and all dimensions by exact binary linear algebra.
3. Build \(G_C,S_C\) and, if used, the outer/source-derived generators; compute the rank profile before making any synchronization claim.
4. Choose \(b_X\in D_X\setminus C_X\), initially the coefficient vector of \(g_{D_X}(x)\), and compute the quotient/annihilator order.
5. Determine the actual fixed-check space \(F_X\) and nuisance set \(\mathcal U_X\) from the symplectic gauge-fixing calculation.

### H.2 Initial hybrid-subsystem code

1. Construct the nonabelian or abelian Pauli group dictated by \(C_X,C_Z\); do not impose \(C_Z^\perp\subseteq C_X\) unless testing the stabilizer-limit regression.
2. Construct the outer gauge/label structure from \(D_X,D_Z\) using the source's general CSS hybrid-subsystem construction, while checking every source hypothesis against the actual tuple.
3. Compute a symplectic hyperbolic basis independently of the arbitrary input generator basis.
4. Apply the fixed-marker gauge-fixing profile and recompute \(S_F,G_F,L_F\).
5. Identify logical-qubit, gauge-qubit, and classical-label pairs. Reject the tuple if any claimed sector has rank zero or if the commutation table is inconsistent.

### H.3 Marker and block extension

For each allowed classical label, apply the X-type marker \(X(b_X)\) (or a verified marker representative in the same sector), attach \(a_l\) left and \(a_r\) right ancillas in \(|0\rangle\), and apply the inherited cyclic boundary CNOT extension. The marker is not counted as an extra classical bit unless that resource change is explicitly declared and compared.

The extension is accepted only if the marker checks used in the proof are the checks actually measured by the receiver. If multiple candidates exist, select deterministically by maximum verified actual period, then lexicographic generator/marker order.

### H.4 Receiver procedure

For a received block with unknown displacement \(\alpha\in[-a_l,a_r]\):

1. select the current n-qubit window;
2. correct X-type window errors with the verified outer decoder, under the source's window-weight assumption;
3. measure the fixed marker-check matrix \(H_{F_X}\) and decode the shift using the direct joint map (G-syndrome), not a quotient surrogate;
4. realign the block;
5. correct X- and Z-type errors using the verified final dressed distances;
6. remove the marker and undo the extension; and
7. decode the quantum, gauge, and classical sectors according to \(S_F,G_F,L_F\).

The proof and simulator must distinguish a stabilizer residual, a gauge residual, a label change, and a logical change.

## I. Expected lemmas, theorems, and propositions — TO-BE-PROVED

Every item below is a **target**, not an established theorem. The Gate 1 rank calculation and the Gate 2 correction are audit results, not claimed construction theorems.

### Target I1: corrected four-code rank theorem or obstruction

For tuples satisfying (G-static), the selected outer condition, and the source's actual hybrid-subsystem hypotheses, derive the final \(S_F,G_F,L_F\) by symplectic reduction. Prove the claimed \((k,m,r)\) formulas, or give a rigorous obstruction showing which desired payload cannot coexist with the marker checks. The theorem must not use \(C_Z^\perp\subseteq C_X\) as a hidden assumption.

### Target I2: exact marker theorem

(a) **Pure-marker case.** For \(F_X=C_X^\perp\), \(b_X=g_{D_X}\), and \(\mathcal U_X\subseteq C_X\), prove that the measured syndrome is represented by \(x^{-\alpha}\bmod f_X\) and that

\[
 a_l+a_r<\operatorname{ord}(f_X)
\]

is sufficient for all allowed shifts to be distinct.

(b) **General case.** For arbitrary admissible \(F_X\) and \(\mathcal U_X\), prove injectivity of the map (G-syndrome) modulo gauge equivalence, or derive the exact annihilator/order condition when \(F_X\) is cyclic. A collision between a shift and a label is a failed candidate, not an ignored edge case.

### Target I3: asymmetric distance proposition

Derive the final dressed X/Z distance expressions from (G-distance) after gauge fixing. Determine when any source-inspired four-code coset expression is equal to the final distance and when it is only a lower bound. Include label-changing operators in the harmful set unless the decoding task says otherwise.

### Target I4: BCH instantiation theorem

For a stated family of primitive binary BCH defining sets, prove or certify:

* all four inclusions and disjointness conditions;
* the selected outer commutation condition;
* the dimensions from cyclotomic cosets;
* exact or explicitly certified final dressed distances; and
* the actual marker period/order, including exceptional factor cases.

No infinite-family theorem is to be claimed until the index ranges, reciprocal cosets, rank profile, and nuisance set have been checked symbolically.

### Target I5: symmetric regression proposition

When the tuple is specialized to the same-pair source setting, reproduce the source's common-pair QSC and hybrid/subsystem profiles by the source's own hypotheses and encoding map. Separately verify that the inner rank formula here gives \(r_C=0\) whenever the source setting imposes \(C^\perp\subseteq C\). Any nonzero source gauge resource must be identified as arising from the outer/fixed-gauge construction, not attributed to a false inner-rank formula.

### Target I6: resource-profile proposition

For a fixed four-code tuple, characterize which complement dimensions can be allocated to fixed marker checks, gauge pairs, and classical labels. State a resource identity only after deriving it from ranks and the actual fixed-check profile; compare it with, but do not assume, the 2024 common-pair identity.

## J. Detailed derivation and proof roadmap

### J.1 Classical algebra

* Use defining-set tests for cyclic inclusion and Euclidean dual containment only where the selected theorem requires them.
* Verify (G-static), including both omitted disjointness conditions, by direct set/matrix operations.
* Independently divide generator polynomials and verify the quotient reconstructs \(g_{C_X}\).
* Compute \(f_X\), the annihilator \(\phi_{F_X,b_X}\) when defined, and their orders by factor orders and direct modular powering.
* Verify every dimension by both generator-matrix rank and cyclotomic-coset counts.

### J.2 Symplectic construction

* Form binary symplectic matrices for \(S_C,G_C\), outer/source generators, fixed marker checks, label operators, and gauge-fixing operators.
* Check every claimed commutator with \(\Omega=\begin{bmatrix}0&I\\I&0\end{bmatrix}\).
* Verify \(S_F\subseteq G_F\), \(S_F\subseteq G_F^\perp\), and the expected commutator rank of \(G_F\).
* Compute \(k,m,r\) from ranks and compare them with any symbolic formulas.
* Test invariance under independent changes of generator and hyperbolic bases.

### J.3 Marker proof

The proof must explicitly derive

\[
H_{F_X}O(b_X+u,-\alpha)^T
\]

for the actual fixed check space and every allowed nuisance class. The required steps are:

1. show that preliminary X correction removes the window error without changing the declared marker/label class;
2. express each shifted marker as a cyclic polynomial shift;
3. in the pure case, divide by \(g_{D_X}\) and reduce modulo \(f_X\); in the general case, use the annihilator or direct matrix map;
4. prove that equal observations imply equal shifts after quotienting declared gauge equivalence; and
5. prove that no allowed classical label has the same syndrome as a different shift.

The fifth step is the principal mathematical risk and is not supplied by the common-pair proof.

### J.4 Pauli correction proof

After realignment, prove that the outer X decoder corrects the allowed window errors and that the final X/Z decoders correct the full-block errors up to (G-distance). The proof must distinguish:

* a stabilizer error, which is harmless;
* a gauge error, which is harmless within a subsystem sector;
* a classical-label-changing error, which is not harmless; and
* a logical error, which is not correctable.

### J.5 Small-instance exhaustive proof audit

For the smallest valid instances, enumerate all Pauli errors below the claimed weights, all allowed shifts, and all declared label representatives. Directly verify the hybrid Knill–Laflamme condition sector by sector and verify that no two shift/label classes have the same measured marker syndrome. These checks are independent of the symbolic proof and are not a substitute for it.

## K. Exact computational and algorithmic workflow

### K.1 Deterministic code factory

Inputs: field \(\mathbb F_2\), length \(n\), four defining sets or generator polynomials, and a marker/gauge profile.

Outputs: generator/parity-check matrices, duals, inclusion and disjointness certificates, dimensions, factor/annihilator orders, symplectic matrices, rank profile, final dressed distances, actual shift/label syndrome table, and a pass/fail reason.

Required operations:

* binary polynomial addition, multiplication, division, gcd, reciprocal, and factor handling;
* cyclotomic-coset generation;
* binary Gaussian elimination;
* cyclic shift and polynomial remainder;
* symplectic rank and commutation checks;
* exact low-weight/coset-distance search; and
* direct syndrome collision enumeration.

The first implementation should use the Python standard library plus a small self-contained GF(2) module. SageMath and Magma may be used as independent validators, not as the only implementation.

### K.2 Four-code search

```text
for extension_degree mu in preregistered_range:
    n = 2^mu - 1
    build all allowed primitive BCH defining intervals
    for (C_X, C_Z, D_X, D_Z) in deterministic_order:
        if not verify_G_static_and_selected_outer_condition(): continue
        build_source_and_inner_symplectic_generators()
        for marker b_X in deterministic_marker_candidates:
            if b_X in C_X: continue
            compute f_X and candidate annihilator/order
            derive_fixed_check_space_and_nuisance_set()
            if symplectic_gauge_fix_or_commutation_test_fails(): continue
            if actual_shift_label_map_has_collision(): continue
            compute k, m, r and final dressed d_X, d_Z
            if no_positive_quantum_or_hybrid_payload(): continue
            save certificate and candidate
return Pareto_frontier(candidates)
```

No random search is needed for the first paper. If a randomized hyperbolic-basis routine is used for exploration, the final certificate must be regenerated deterministically.

### K.3 Exact-distance modes

1. **Exhaustive mode:** enumerate all codewords and all relevant normalizer cosets when the dimension is below a fixed, recorded threshold.
2. **Meet-in-the-middle mode:** split generator rows and search for low-weight vectors for moderate dimensions.
3. **Certified BCH mode:** invoke only explicit-distance conditions proved in the paper or in a cited source, with all hypotheses checked.
4. **Bound-only mode:** retain lower bounds for exploration but exclude those points from any “exact parameter” table.

### K.4 Shift-syndrome verifier

For every candidate, every allowed \(\alpha\), and every declared nuisance/label representative:

1. build the shifted marker vector;
2. compute the syndrome using the actual measured matrix \(H_{F_X}\);
3. independently compute the polynomial residue when the pure/annihilator hypotheses apply;
4. compare all pairs \((\alpha,\text{label/gauge class})\); and
5. record collisions with the responsible representative and the failed condition.

Gauge-equivalent representatives must be collapsed before declaring a collision or an injective map.

### K.5 Code-capacity simulator

Use an explicitly defined biased Pauli model, for example independent X and Z components with probabilities \(p_X,p_Z\), or a fully specified \(p_I,p_X,p_Y,p_Z\) model. State which model is used; do not call independent components a depolarizing channel.

For each trial:

1. sample a legal shift;
2. sample Pauli supports and enforce or record the window-weight condition;
3. run the syndrome/marker decoder;
4. check whether the residual lies in the allowed stabilizer/gauge group and preserves the classical label and logical state; and
5. record synchronization failure, X logical failure, Z logical failure, label failure, and total failure separately.

Gate and measurement faults are excluded from the central experiment and must be listed as a limitation.

## L. Feasible parameter-selection strategy

### L.1 Primary family

Use primitive binary BCH codes of length

\[
 n=2^\mu-1,
\]

initially with \(\mu\in\{5,6,7,8,9\}\), subject to runtime and exact-distance certification. The search must not impose \(C_Z^\perp\subseteq C_X\) unless it is intentionally measuring the stabilizer-limit regression, because that inclusion forces the inner rank \(r_C=0\).

The pre-registered search order is:

1. maximize verified **actual** marker period/order;
2. retain only positive logical and intended hybrid-subsystem payloads after gauge fixing;
3. maximize the biased-channel-relevant final distance pair \((d_Z^F,d_X^F)\) lexicographically for a declared \(p_Z/p_X\);
4. maximize \(k+m+r\) only after the previous filters; and
5. report the full Pareto frontier rather than a single cherry-picked point.

### L.2 BCH four-code geometry

The first restricted search uses

\[
 C_X\subseteq D_X,\qquad C_Z\subseteq D_Z,
\]

and may use the scaffold \(C_Z\subseteq C_X\) or \(D_Z\subseteq D_X\) to enumerate manageable tuples. Such nesting does not replace (G-static), the outer commutation check, or the symplectic rank test. The search records defining sets rather than assuming that designed distance equals true distance.

A first unit-test target is a small tuple with four roles drawn from the \(n=31\) BCH chain, with distinct or partially coincident design intervals chosen to test both positive and zero inner-gauge ranks. This is a test target, not a claimed parameter set or result. It must pass all rank, actual-order, and distance checks before appearing in any result table.

### L.3 Synchronization allowance

For each certified candidate, evaluate:

* the maximal total allowance implied by the actual period (with the source's off-by-one convention stated explicitly);
* balanced splits; and
* deliberately one-sided splits.

Do not compare only \(a_l+a_r\) if the decoder or physical application is directionally asymmetric.

### L.4 Excluded parameter claims

No numerical family, rate, distance, or improvement is promised in advance. If only lower bounds can be certified, the manuscript must label them as lower bounds. If the corrected rank profile produces no hybrid-subsystem payload for the BCH range, the direction fails its feasibility gate rather than being padded with unverified examples.

## M. Validation protocol and acceptance criteria

### M.1 Algebraic checks

* generator divisibility and code inclusion;
* both omitted disjointness conditions in (G-static);
* dual containment by reciprocal generator and by matrix orthogonality wherever required;
* dimensions by two independent rank methods;
* quotient, annihilator, and actual marker period by independent methods;
* final fixed-check isotropy and gauge commutator rank;
* shift/label injectivity using the actual measured matrix; and
* final dressed-distance computation by direct normalizer/gauge coset search for small instances.

### M.2 Symmetric regression tests

Run the source's common-pair construction with its own hypotheses and then run the corrected four-code code factory on the symmetric specialization. Recover the source's published synchronization syndrome and resource profile, while separately recording that the inner formula (G-ranks) gives zero inner gauge rank under \(C^\perp\subseteq C\). A failure of the source regression blocks all asymmetric claims.

### M.3 Go/no-go validation gate

The project proceeds to a manuscript only if it has:

1. a proved marker theorem or a rigorously characterized obstruction under the corrected conditions;
2. at least one nontrivial four-code rank profile with a positive intended payload;
3. an independently reproduced actual syndrome/order certificate;
4. exact or explicitly certified final dressed distances for all headline points;
5. a fair comparison at fixed field, block length, payload constraints, and synchronization allowance; and
6. a closed publication-level novelty search, including the currently OPEN database records.

Until these conditions hold, the blueprint remains a research plan and not a final result.

## N. Independent cross-check plan

### N.1 Exhaustive quantum cross-check

For small \(n\), construct the full stabilizer/gauge groups and test all Pauli errors through the claimed X/Z weights. For each allowed shift and every classical-label representative, verify that the decoder returns the correct boundary and that the residual is an allowed stabilizer or gauge operator. Verify separately that a label-changing residual is counted as failure.

### N.2 Independent software cross-check

At least one of the following must reproduce the final certificates without importing the main implementation's code:

* SageMath finite-field/cyclic-code routines;
* Magma cyclic-code and minimum-distance routines; or
* a second small plain-Python implementation written from the saved defining sets.

The independent implementation must reproduce both the direct symplectic syndrome table and the polynomial/annihilator calculation whenever the latter is applicable. Published source examples should be reproduced first, including at least one explicit-distance BCH or Whiteman example.

### N.3 Statistical simulation

Use fixed seeds, report the number of trials and confidence intervals, and separate synchronization, label, X-logical, Z-logical, and total failure. Simulation is evidence of operational behavior under the stated model, not a proof.

## O. Benchmark and comparison plan using reputable indexed literature

The benchmark table must contain source citations, source assumptions, and comparability flags. Initial rows are:

| Benchmark | What it establishes | Fair comparison variables |
|---|---|---|
| Fujiwara 2013 QSC theorem | Common cyclic CSS synchronization and windowed recovery | Same \(q,n,a_l,a_r\), quantum payload, X/Z correction model. |
| Fujiwara–Tonchev–Wong 2013 | Order can reach \(n\) through primitive factors; BCH/RM families | Same order and classical code lengths. |
| QR augmentation source | Prime/Mersenne-prime maximum-order binary constructions | Same binary length and synchronization allowance. |
| La Guardia 2011 asymmetric BCH | Separate X/Z CSS distances without synchronization | Same \((n,k,d_Z/d_X)\), with synchronization marked absent. |
| Shi–Yue–Huang 2021 | Whiteman maximum-order cyclic examples, including published \(n=35\) tables | Same q, n, order, and classical distance certificate. |
| Liu–Kai 2023 | Explicit-distance QSC examples, including \(q=7,n=2400\) and \(q=5,n=624\) | Same q, n, QSC payload, phase/bit correction. |
| Du–Ma–Liu 2023 | Repeated-root QC QSCs | Same length and distance-certification type; do not compare cyclic and QC rate without noting structure. |
| Wang–Zhou 2025 | Most recent explicit-distance BCH QSCs and length lifting | Same q,n, exact-distance status, and order. |
| Tansuwannont–Nemec 2024/2026 | Common-pair subsystem/hybrid/hybrid-subsystem tradeoffs | Same \(n,k,m,r,d\) and synchronization distance; asymmetric points must not be compared to a different payload class. |

The Grassl online code tables used by source papers may be used only with a recorded access date, snapshot, version/hash where possible, and a clear distinction between a published theorem and an online benchmark. No unpublished dataset is to be invented.

### O.2 External novelty matrix (current, qualified)

The following matrix records the closest accessible sources as of 2026-09-25. “No” means that the inspected source does not supply the listed component; it is not evidence that no uninspected paper does. The target column is the exact intersection: **independent X/Z cyclic pairs + provably unique marker + hybrid/subsystem gauge/classical trade-off**.

| Source | Independent X/Z asymmetric protection | Synchronization marker/order proof | Subsystem or hybrid resource | Four-code asymmetric synchronized theorem | What remains absent relative to target |
|---|---:|---:|---:|---:|---|
| Fujiwara, *Block synchronization for quantum information* (PRA 87, 022344, 2013), DOI [10.1103/PhysRevA.87.022344](https://doi.org/10.1103/PhysRevA.87.022344) | No, common CSS chain | Yes | No | No | Independent X/Z hybrid marker and gauge analysis. |
| Fujiwara–Tonchev–Wong, *Algebraic techniques...* (PRA 88, 012318, 2013), DOI [10.1103/PhysRevA.88.012318](https://doi.org/10.1103/PhysRevA.88.012318) | No, common cyclic pair | Yes, quotient order | No | No | Same as above. |
| Aly, *Asymmetric and Symmetric Subsystem BCH Codes and Beyond* (arXiv:0803.0764) | Yes | No | Yes, asymmetric subsystem | No | No block-synchronization marker theorem. |
| Aly–Ashikhmin, *Nonbinary Quantum Cyclic and Subsystem Codes Over Asymmetrically-decohered Quantum Channels* (arXiv:1002.2966) | Yes | No | Yes, asymmetric subsystem | No | No shift-syndrome/order construction. |
| La Guardia, *New families of asymmetric quantum BCH codes* (QIC 11, 239–252, 2011) | Yes | No | No hybrid marker | No | No synchronization and no gauge-fixed marker. |
| Tansuwannont–Nemec, *Synchronizable hybrid subsystem codes* (arXiv:2409.11312; IEEE TQE 2026 DOI [10.1109/TQE.2026.3673092](https://doi.org/10.1109/TQE.2026.3673092)) | General CSS spaces appear in the hybrid framework, but the synchronization construction is common-pair | Yes for common pair | Yes | **Near match, not established exact match** | Independent X/Z marker injectivity and corrected nuisance/rank conditions are not supplied as the target theorem. Final journal diff is OPEN. |
| Dinh–Nguyen–Tansuchat, *Quantum MDS and synchronizable codes...* (AAECC 34, 931–964, 2023), DOI [10.1007/s00200-021-00531-6](https://doi.org/10.1007/s00200-021-00531-6) | No independent hybrid X/Z marker | Yes | No | No | No four-code hybrid-subsystem construction. |
| Du–Ma–Liu, *Quantum synchronizable codes from repeated-root quasi-cyclic codes* (CAM 42, 161, 2023), DOI [10.1007/s40314-023-02298-7](https://doi.org/10.1007/s40314-023-02298-7) | Not as the target four-code asymmetric CSS object | Yes for QC construction | No target hybrid resource | No | A QC/QSC mechanism is not the proposed four-code marker theorem. |
| Wang–Zhou, *BCH codes with explicit minimum distance and applications in QSCs* (Cryptogr. Commun. 17, 1427–1443, 2025), DOI [10.1007/s12095-025-00815-5](https://doi.org/10.1007/s12095-025-00815-5) | No independent X/Z hybrid marker | Yes | No | No | Common-pair explicit-distance baseline only. |

**Matrix conclusion:** the target is a defensible unresolved intersection in the accessible record, but the matrix is not a first-publication claim. The four-code general CSS material in the 2024/2026 source is a near-exact prior and must be cited as such; the proposed novelty, if any, is specifically the independent X/Z **synchronization proof after rank-derived gauge fixing**, not the existence of four classical spaces alone.

### O.3 Search record

| Date | Accessible source/index | Query family | Result/action |
|---|---|---|---|
| 2026-09-25 | arXiv and publisher pages | `"asymmetric quantum synchronizable"`; `"synchronizable" AND "hybrid subsystem"`; `"synchronizable" AND "asymmetric CSS"` | Located the common-pair 2024/2026 source, asymmetric subsystem/cyclic sources, and ordinary QSC papers; no exact target match identified. |
| 2026-09-25 | Crossref API and OpenAlex metadata search | title/abstract combinations of `asymmetric`, `quantum synchronizable`, `hybrid`, `subsystem` | Metadata triage; no exact target title/record located. This is not a full-text absence proof. |
| 2026-09-25 | IEEE Xplore search results accessible through web search | `site:ieeexplore.ieee.org "synchronizable hybrid subsystem"`; `site:ieeexplore.ieee.org "asymmetric" "quantum synchronizable"` | Returned unrelated hybrid-systems results and ordinary QSC/AQEC papers; no exact target match in the accessible results. |
| 2026-09-25 | Springer/arXiv indexed pages | asymmetric QSC, asymmetric subsystem, synchronizable cyclic/QC, hybrid subsystem | Confirmed the rows in O.2 and the source-chain distinctions. |
| 2026-09-25 | Web of Science, Scopus, MathSciNet, zbMATH direct records | exact and synonym queries listed in V | **OPEN:** direct query/export logs were not available in this environment; must be completed before a novelty claim. |


## P. Expected tables and figures

### Tables

1. **Source audit:** construction type, field, length family, order proof, distance status, and limitation.
2. **Four-code certificates:** \((C_X,C_Z,D_X,D_Z)\), defining sets, dimensions, (G-static) checks, marker, actual fixed-check space \(F_X\), nuisance set, quotient/annihilator/order, and rank profile.
3. **Exact distance status:** final \(d_X^F,d_Z^F\), proof/certificate method, and whether each value is exact or a lower bound.
4. **Resource profiles:** \((k,m,r,d_Z^F/d_X^F,S_{\rm actual})\) for every Pareto point.
5. **Symmetric regression:** source common-pair values and corrected-code-factory values, with the inner-rank obstruction explicitly shown.
6. **Published benchmarks:** only comparable rows with citations and assumptions.
7. **Failure ledger:** rejected tuples and the exact failed condition, especially rank collapse, non-isotropic gauge fixing, and shift/label collisions.
8. **Simulation:** channel parameters, trials, confidence intervals, and separate failure modes.
9. **Novelty/search matrix:** query, index, date, hit classification, and unresolved source requests.

### Figures

1. Four-code inclusion lattice and the distinction between static spaces and final fixed/gauge spaces.
2. Symplectic commutation diagram showing inner group, outer/source generators, marker checks, and classical labels.
3. Shift-syndrome points \((\alpha,u)\mapsto\sigma_{\alpha,u}\) and any collision boundary.
4. Pareto frontier in \((d_Z^F,d_X^F,k+m+r,S_{\rm actual})\) space.
5. Logical/label/synchronization failure rates versus biased noise.
6. Decoder flow: window X correction → actual marker syndrome → realignment → full CSS/hybrid-subsystem correction.

## Q. Reproducibility plan

The eventual implementation must include:

* a `pyproject.toml` or equivalent environment specification;
* exact Python/Sage/Magma version information;
* a machine-readable defining-set input for every candidate;
* deterministic seed and search-order files;
* one command to regenerate all certificates and tables;
* separate scripts for the main implementation and independent cross-check;
* serialized polynomial, matrix, rank, order, and distance certificates;
* unit tests for all published source examples used as regressions;
* simulation configuration files containing channel model, trial count, seed, and confidence method; and
* a README explaining which outputs are theorem-certified, source-reproduced, computed exact values, lower bounds, or exploratory data.

Generated large search outputs should remain outside Git unless compact and required; summarized certificates and small test fixtures may be versioned. The repository currently has no ignore convention beyond its minimal README, so the implementation phase must add one before generating large artifacts.

## R. Risks, failure modes, and explicit stop conditions

### Mathematical risks and failure modes

1. **Marker checks may be gauge operators rather than fixed stabilizers.** The proposed profile may consume too much payload or may not commute with all classical labels.
2. **The four-code quotient may not control the actual syndrome.** The correct object may be \(\phi_{F_X,b_X}\) or a direct joint map rather than \(g_{C_X}/g_{D_X}\).
3. **Free gauge/label components may collide with shifts.** A candidate fails unless they are invisible under the fixed checks or are separated by a proved joint injectivity condition.
4. **Outer correction may not use a raw distance.** Final distances must be the dressed normalizer/gauge distances after gauge fixing.
5. **Positive hybrid-subsystem ranks may be rare.** If all small BCH tuples collapse to a stabilizer core or a zero-payload code, the proposed family is not computationally feasible as stated.
6. **The common-pair specialization may fail under a careless basis choice.** Any such failure is an implementation/proof error until independently resolved.
7. **A near-exact prior may close the gap.** The 2024/2026 source's general four-space framework must be compared line by line; if it already proves the corrected target, the direction must change rather than be cosmetically renamed.

### Explicit stop conditions

* If the corrected marker theorem is false and no useful obstruction theorem is available, stop the direction.
* If no tuple has positive intended payload and certified final distances in the preregistered range, stop rather than enlarge the scope silently.
* If a prior paper contains the same independent-X/Z marker-compatible theorem, stop and redesign the question.
* If direct database searches materially change O.2, remove or rewrite all novelty language.

## S. Required inputs and OPEN items

### Required external inputs and evidence

1. **Final 2026 source text:** obtain and diff the IEEE TQE version, DOI 10.1109/TQE.2026.3673092, against local `2409.11312v2.pdf`; update theorem numbering, notation, and any post-review corrections. **OPEN.**
2. **Publication-level novelty sweep:** export query results from IEEE Xplore, Web of Science, Scopus, MathSciNet, and zbMATH using the exact/synonym queries in V; store query date, filters, result count, and screened records. **OPEN.**
3. **Prior asymmetric QSC claims:** check books, theses, conference proceedings, and non-English indexing for “asymmetric quantum synchronizable code,” “asymmetric QSC,” “synchronizable asymmetric CSS,” and “asymmetric hybrid subsystem synchronization.” **OPEN.**
4. **Author artifacts:** no source code or datasets were found in the repository. Verify whether the 2023/2025 Magma checks or code tables have public supplementary files; if not, reproduce them independently. **OPEN.**
5. **Exact source hypotheses:** page-level recheck of all BCH, repeated-root, and hybrid-subsystem statements whose temporary extraction loses reciprocal symbols, floors, or rank qualifiers. **OPEN.**
6. **Journal status:** verify current SCIE indexing, JCR quartile, and top-10-percentile status of the target venue at submission time rather than relying on a static claim. **OPEN.**

### Closed evidence at this blueprint revision

* `Quantum Synchronizable.zip` passes `unzip -t`.
* The local source PDFs and source-derived text were reviewed.
* The corrected Gate 1 rank obstruction and Gate 2 syndrome issue are recorded above.
* The accessible external matrix in O.2 has been assembled, but it is explicitly qualified and does not authorize a novelty claim.

### Scope limits and stop conditions

* fault-tolerant syndrome extraction;
* gate/measurement noise;
* qudit generalization;
* repeated-root/QC replacement of the BCH family;
* deletion/loss synchronization; and
* an unproved universal resource optimality theorem.

If any excluded topic becomes necessary for the proof, stop and re-scope rather than silently enlarging the paper. Until the OPEN inputs above are closed, the blueprint cannot be labeled FINAL.

## T. Target journal class and technical-fit rationale

**Primary target:** *IEEE Transactions on Information Theory* or an equivalently selective, SCIE-indexed top coding/information-theory journal. The paper must meet a Q1/top-10%-quartile standard at the time of submission, with a theorem-level contribution, independently reproducible computations, and fair published benchmarks.

**Secondary fit, only if the hybrid-subsystem interpretation has clear quantum-information significance:** *Physical Review A* or a comparably selective quantum-information journal. The journal choice must be rechecked using current JCR/Scimago/Web of Science records; no quartile claim is made in this blueprint.

The 2026 *IEEE Transactions on Quantum Engineering* version of the source paper is an essential benchmark and possible venue context, but the proposed paper should not target it merely because it extends that source; the expected contribution should be judged against the stronger coding-theory standard.

## U. Section-by-section manuscript architecture

1. **Introduction and contribution boundary** — define QSC, asymmetric CSS, hybrid subsystem; state that the four-code theorem is new work and list what is inherited.
2. **Source framework and notation** — cyclic order, CSS distances, hybrid-subsystem ranks, and the code-capacity model.
3. **Marker-compatible four-code framework** — precise conditions, gauge-fixing profile, and rank definitions.
4. **Synchronization theorem** — shifted stabilizer/gauge derivation, syndrome injectivity, and edge cases.
5. **Asymmetric distance theorem** — dressed X/Z distances and conditions for exactness.
6. **BCH construction** — defining sets, dual containment, order, dimensions, and explicit-distance certificates.
7. **Algorithms and implementation** — code factory, search, decoder, exact-distance modes, and independent verifier.
8. **Validation** — source regressions, exhaustive small instances, symplectic cross-checks, and code-capacity simulations.
9. **Benchmarks and novelty test** — fixed-resource comparisons and external-literature audit.
10. **Limitations and future work** — fault tolerance, q-ary/QC families, and unresolved optimization/optimality questions.
11. **Appendices** — polynomial proofs, rank lemmas, code listings/pseudocode, certificates, and full rejected-candidate ledger.

Every theorem statement should carry one of three labels in the drafting workflow: **inherited**, **extended target**, or **new proved result**.

## V. Explicit nontrivial novelty test

A novelty claim is allowed only if all five gates pass. The current document records a **NO-GO for FINAL** status because S1 is not fully archived and the corrected mathematical gates are still targets.

### V.1 Publication-level literature gate

Before drafting the abstract, run and archive searches across the databases in Section S using at least:

* `"asymmetric quantum synchronizable"`;
* `"asymmetric" AND "quantum synchronizable code"`;
* `"synchronizable" AND "hybrid subsystem" AND CSS`;
* `"synchronizable" AND "asymmetric CSS"`;
* `"quantum synchronizable" AND (C_X OR C_Z OR four codes)`; and
* equivalent searches for `misalignment`, `block synchronization`, `gauge fixing`, `hybrid stabilizer`, and `subsystem`.

Read every exact or near-exact hit, including dissertations and conference papers. O.2 records the accessible search and its limitations. If an exact prior is found, stop and change direction.

### V.2 Corrected containment/rank gate

Implement a source-reproduction map for (G-static), the exact source hybrid-subsystem hypotheses, and the final symplectic rank profile. The proposed construction fails novelty/validity if every candidate either:

* collapses to the discarded \(C_Z^\perp\subseteq C_X\) stabilizer limit with \(r_C=0\);
* is a symmetric specialization \(C_X=C_Z,D_X=D_Z\);
* is only a generator or hyperbolic-basis change;
* violates either disjointness condition or the actual outer commutation test; or
* is an already published QC/ring/constacyclic construction without a new marker proof.

### V.3 Structural gate

At least one headline candidate must satisfy all of:

\[
 C_X\ne C_Z,
 \qquad
 D_X\ne D_Z\ \text{or a provably asymmetric fixed-marker profile},
\]

with nonzero quantum payload, nonzero intended hybrid-subsystem payload, and independently verified final X/Z dressed distances not forced equal by the common-pair specialization. It must also pass the actual shift/label injectivity test.

### V.4 Strict comparison gate

At fixed field, physical length, actual synchronization allowance, and comparable payload, the new point must show a strict improvement in at least one meaningful quantity—such as a protected biased-sector distance, quantum/classical/gauge payload, or verified marker period—without being worse in every other reported quantity. If only a different tradeoff exists, report it as a tradeoff, not as “better.”

### V.5 Proof and implementation gate

The corrected marker theorem or obstruction, rank/distance definitions, source regression, independent implementation, exhaustive small-instance checks, and the completed literature record must all pass. A parameter table without the four-code synchronization proof is not a novelty result.

**Decision rule:** if V.1–V.5 do not all pass, the manuscript must state “candidate direction rejected or unresolved” and must not claim a new asymmetric synchronizable hybrid-subsystem code.

# Final five-component summary

1. **Research question:** Can independently selected X/Z cyclic code pairs retain a provably unique quantum synchronization marker after the rank-defined gauge construction, while preserving an asymmetric X/Z distance pair and a nonzero hybrid-subsystem resource?
2. **Mathematical contribution sought:** A corrected four-code theorem—or a rigorous obstruction—for \((C_X,C_Z,D_X,D_Z)\) with source disjointness, symplectic rank-defined \((k,m,r)\), final dressed \((d_Z,d_X)\), and an actual shift/label injectivity condition. The former mandatory \(C_Z^\perp\subseteq C_X\) package is rejected because it forces the inner gauge rank to zero.
3. **Construction and computation:** Primitive binary BCH four-code tuples, exact inclusion/disjointness/order/rank checks, actual fixed-check and nuisance-set derivation, certified or exact dressed distances, deterministic Pareto search, and code-capacity decoding simulation.
4. **Validation standard:** Symmetric-source regression, independent polynomial/annihilator and symplectic implementations, exhaustive small-instance Pauli/shift/label checks, published QSC/AQECC benchmarks, and a completed archived external novelty search.
5. **Go/no-go and publication target:** Current status is **NO-GO for FINAL**. Proceed only if the corrected Gate 1 and Gate 2 proof/obstruction, positive nontrivial ranks, certified distances, independent checks, and V.1–V.5 novelty gates pass; target a Q1/top-10%-standard coding/information-theory journal, with current indexing verified at submission.

# Complete A–V execution checklist

| Section | Required deliverable before manuscript drafting |
|---|---|
| A | Final title that accurately describes the proved object. |
| B | One precise research problem and one central question. |
| C | Literature/source gap supported by the complete source audit and external-search plan. |
| D | Source-paper foundation with inherited, extended, and genuinely new work separated. |
| E | One theorem-level contribution, not a cosmetic parameter change. |
| F | Falsifiable hypotheses and explicit rejection criteria. |
| G | Corrected four-code static conditions, actual marker-check/nuisance definitions, symplectic ranks, distances, and noise model. |
| H | Encoder, marker, gauge-fixing, extension, and decoder specification. |
| I | Proved-or-rejected theorem/proposition targets, never assumed results. |
| J | Algebraic, symplectic, marker, distance, and edge-case derivation roadmap. |
| K | Deterministic code factory, search, order, distance, decoder, and simulator algorithms. |
| L | Justified BCH ranges, filters, and Pareto selection rules. |
| M | Validation protocol, acceptance criteria, and code-capacity model. |
| N | Independent polynomial, symplectic, exhaustive, and software cross-checks. |
| O | Fair benchmark table using reputable indexed literature and comparability flags. |
| P | Parameter/resource/failure tables and syndrome/Pareto/decoder figures. |
| Q | Versioned environment, inputs, seeds, certificates, and regeneration commands. |
| R | Risks, failure modes, stop conditions, and documented go/no-go decision. |
| S | Exact external source files, publisher version, database searches, and other OPEN inputs. |
| T | Current SCIE/JCR/top-10-percentile verification and technical-fit rationale. |
| U | Manuscript sections with inherited, target, and proved-result labels. |
| V | Completed five-gate nontrivial novelty test; current status remains NO-GO until the OPEN search records and corrected proof gates close. |
