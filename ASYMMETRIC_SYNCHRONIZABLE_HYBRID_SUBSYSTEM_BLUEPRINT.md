# Research blueprint: asymmetric synchronizable hybrid-subsystem CSS codes

**Repository:** `arunyadav0307-stack/QSC`  
**Branch:** `arena/01a0d961-qsc`  
**Blueprint date:** 2026-09-25 (UTC)  
**Evidence status:** research hypothesis and implementation plan. No new theorem, parameter set, novelty claim, or computational result is asserted in this document.

## Scope and evidence discipline

This blueprint was prepared after reading all 12 PDFs in `Quantum Synchronizable.zip`, with priority given to the 2024 synchronizable hybrid-subsystem paper, the 2025 explicit-distance BCH paper, and the 2023 quasi-cyclic paper. The repository contains no implementation, benchmark dataset, or author-supplied computational artifact. The temporary extracted text used during review is outside the repository and is not a deliverable.

The central proposal is deliberately narrower than “all asymmetric QSCs” and deliberately stronger than a notation change:

> **Replace the single cyclic chain \(\mathcal C^{\perp}\subset\mathcal C\subset\mathcal D\) by separately designed X- and Z-sector classical pairs, then prove that a marker syndrome remains injective after the gauge/hybrid construction.**

The intended primary object is an **asymmetric synchronizable hybrid-subsystem CSS code**. A synchronizable asymmetric CSS stabilizer core is the mandatory first milestone; the hybrid-subsystem lift is not to be claimed unless its gauge-fixing and marker proof pass the gates in Sections H, I, L, and P.

The notation below distinguishes:

* **Inherited:** already proved or constructed in the cited source papers.
* **Extended:** a direct but nontrivial generalization that still requires a proof in this project.
* **New:** a proposed theorem, family, algorithmic comparison, or empirical result that must not be described as established before completion.

---

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

## Cross-source decision

The following alternatives were considered and rejected as the central direction:

1. **Only another ordinary cyclic QSC family:** already heavily covered by the 2013–2025 sources and not a substantive extension of the latest hybrid-subsystem theorem.
2. **Only a QC/repeated-root QSC:** mathematically useful, but the 2023 source already proves the basic noncyclic-QSC mechanism; a simple transplant would fail the nontrivial novelty test.
3. **A qudit or fault-tolerant construction:** important but requires additional finite-field and circuit-fault infrastructure absent from the repository; reliable validation is not yet feasible within one focused project.
4. **Only a new resource-tradeoff bound:** potentially strong, but the 2024 optimality conjecture is not enough by itself to guarantee an explicit computationally testable code family.

The selected direction combines the strongest recent synchronizable hybrid-subsystem framework with the independent X/Z CSS design problem and exact-distance BCH verification. Its risk is real, but its algebraic conditions and finite-length tests are executable.

---

# A–S research blueprint

## A. Title

**Asymmetric Synchronizable Hybrid-Subsystem CSS Codes from Cross-Nested Cyclic Codes**

Working short title: **ASH-CSS**.

The title does not claim that the construction already exists. It names the object to be proved or rejected.

## B. Precise problem and gap

### Problem

A synchronizable CSS code must do two logically different jobs:

1. correct X- and Z-type Pauli errors; and
2. identify a block displacement from a quantum syndrome without measuring the encoded state destructively.

The common-chain construction controls both jobs through one pair \(\mathcal C\subset\mathcal D\). The latest hybrid-subsystem framework adds gauge and classical sectors, but still uses the same cyclic pair for the marker and for both CSS sectors. Standard asymmetric CSS constructions use distinct classical codes for X and Z protection, but do not prove that their syndrome structure survives quantum block misalignment or the hybrid-subsystem gauge operations.

### Gap statement

The repository contains no proved construction that simultaneously has all four properties:

1. separate X/Z classical code choices;
2. a cyclic-order synchronization marker with a uniqueness proof;
3. a hybrid-subsystem gauge/classical sector; and
4. independently computed X- and Z-distance guarantees.

This is an **internal repository gap**, not yet a publication-level absence claim. A full external novelty search is a mandatory gate in Section S.

### Central research question

> **Can four nested classical cyclic codes \((C_X,C_Z,D_X,D_Z)\), with a marker-compatible gauge-fixing profile, produce a synchronizable hybrid-subsystem CSS code whose shift syndrome is provably injective and whose X/Z distances can be tuned independently?**

The answer may be negative. A negative result caused by an explicit obstruction would still be mathematically useful, but the project must not call a failed construction a new code family.

## C. Reused source foundation

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

## D. Novel contribution

The proposed contribution has one mathematical core and two necessary supporting components.

### Core contribution: a marker-compatible four-code theorem

Let

\[
(C_X,C_Z,D_X,D_Z)
\]

be four binary cyclic codes of length \(n\). The theorem target will identify sufficient conditions under which:

* \(C_Z^\perp\subseteq C_X\) supplies an asymmetric inner CSS structure;
* \(C_X\subseteq D_X\) and \(C_Z\subseteq D_Z\) supply outer correction/gauge sectors;
* the outer pair has the required symplectic commutation, for example \(D_Z^\perp\subseteq D_X\) in the stabilizer-core specialization;
* a marker vector \(b_X\in D_X\setminus C_X\) produces a quotient factor
  \(f_X(x)=g_{C_X}(x)/g_{D_X}(x)\); and
* a gauge-fixing profile makes the needed Z-type marker checks fixed or otherwise observable without revealing logical quantum information.

### Explicit family component

Use primitive binary BCH chains as the first computational family. The code search will choose different defining-distance intervals for the four roles and will certify, rather than assume, dual containment, exact distances, quotient order, and the hybrid-subsystem ranks.

### Reproducible validation component

Produce a public, deterministic implementation that independently checks the polynomial construction, symplectic matrices, shift-syndrome table, exact small-code distances, and code-capacity decoding simulations. Computation supports the theorem and parameter claims; it does not replace the proof.

## E. Questions and hypotheses

### One central question

The central question is the one in Section B. All experiments must serve it.

### Testable hypotheses

* **H1 — marker hypothesis:** under a computable marker-compatible rank condition, the syndrome map
  \[
  \alpha\longmapsto H_{C_X}O(b_X,-\alpha)^T
  \]
  remains injective over \(-a_l\le\alpha\le a_r\), with a sufficient cyclic bound \(a_l+a_r<\operatorname{ord}(f_X)\).
* **H2 — asymmetric-distance hypothesis:** changing \(C_Z\) independently of \(C_X\) changes the dressed Z distance and the quantum/classical/gauge ranks without destroying H1.
* **H3 — rate/usefulness hypothesis:** on a biased code-capacity Pauli channel, at least one certified ASH-CSS Pareto point improves the relevant logical-failure estimate or one of \((k,m,r,d_X,d_Z)\) at fixed \((n,\operatorname{ord}(f_X))\) relative to the common-pair synchronizable hybrid-subsystem baseline.
* **H4 — nontriviality hypothesis:** successful points require genuinely distinct X/Z sectors and cannot be transformed into the 2024 common-pair construction by swapping labels, changing a generator basis, or selecting a different hyperbolic basis.

H1–H4 are hypotheses, not results.

## F. Definitions and mathematical framework

### F.1 Primary field and cyclic ring

The first paper will work over \(\mathbb F_2\) and

\[
R_n=\mathbb F_2[x]/\langle x^n-1\rangle.
\]

The binary restriction is intentional: it makes the symplectic, exhaustive small-length, and shift-syndrome checks independently implementable. A q-ary extension is OPEN and is not part of the acceptance criteria.

A cyclic code is an ideal generated by a divisor \(g(x)\mid x^n-1\). For \(C\subseteq D\), write \(g_D\mid g_C\). The quotient used by the X-marker is

\[
 f_X(x)=\frac{g_{C_X}(x)}{g_{D_X}(x)},
\]

provided the quotient is nonconstant and has nonzero constant term. Its order is the least positive \(e\) with \(f_X(x)\mid x^e-1\).

### F.2 Asymmetric CSS core

For binary linear codes \(C_X,C_Z\subseteq\mathbb F_2^n\), impose

\[
 C_Z^\perp\subseteq C_X.
\]

The inner CSS stabilizer is

\[
 S_{\rm CSS}=\langle X(C_Z^\perp),Z(C_X^\perp)\rangle,
\]

with quantum dimension

\[
 k_{\rm CSS}=k_X+k_Z-n.
\]

The dressed X- and Z-distance targets are

\[
 d_X(C_X,C_Z)=\min\{\operatorname{wt}(u):u\in C_X\setminus C_Z^\perp\},
\]
\[
 d_Z(C_X,C_Z)=\min\{\operatorname{wt}(v):v\in C_Z\setminus C_X^\perp\}.
\]

These are coset distances. Raw classical distances may be used only as certified lower bounds when the relevant containment makes the implication valid.

### F.3 Four-code package

The primary sufficient-condition package to test is

\[
\begin{aligned}
& C_Z^\perp\subseteq C_X,\\
& C_X\subseteq D_X,\qquad C_Z\subseteq D_Z,\\
& D_Z^\perp\subseteq D_X,\\
& b_X\in D_X\setminus C_X.
\end{aligned}
\tag{P}
\]

The outer inclusion may be replaced by the exact symplectic commutation/rank condition if the general hybrid-subsystem basis requires it; no weaker condition may be silently assumed.

The first BCH specialization will use the more restrictive but easy-to-check chain

\[
 C_Z\subseteq C_X\subseteq D_X,
 \qquad C_Z\subseteq D_Z\subseteq D_X,
\]

with each selected code dual-containing. This restriction is a validation scaffold, not the claimed general theorem.

### F.4 Marker-compatible gauge fixing

The latest source shows that synchronization uses fixed Z-type checks representing the inner dual code while some complementary operators may remain gauge or classical-label operators. For the asymmetric construction define a marker-check space \(M_X\) and require:

1. \(M_X\) is represented by fixed Z-type stabilizers in every sector used for synchronization;
2. \(D_X^\perp\subseteq M_X\subseteq C_X^\perp\), with equality \(M_X=C_X^\perp\) in the simplest core construction;
3. any unfixed complement is explicitly included in the gauge group and cannot alter the measured marker syndrome; and
4. the marker vector and any classical label vectors have a symplectic commutation table verified by rank computation.

This is the central technical issue. It is not enough to quote the CSS theorem for the four codes.

### F.5 Concrete marker-compatible gauge-fixing profile

The implementation will use a matrix-level profile rather than assume that the common-pair gauge basis remains valid. Start with the inner/outer stabilizer and gauge generators supplied by the four-code CSS hybrid-subsystem construction. Let \(S_0\) be the common stabilizer matrix, \(G_0\) the full gauge-generator matrix, and let \(L_0\) be the commuting classical-label generator set.

1. Let \(W_X=\{Z(v):v\in C_X^\perp\}\) and \(W_D=\{Z(v):v\in D_X^\perp\}\). Compute independent bases for \(W_X\), \(W_D\), and their images modulo \(S_0\).
2. Gauge-fix the complement \(W_X/W_D\) by adjoining its Z-type basis vectors to the fixed stabilizer. This defines the candidate marker-check space \(M_X=W_X\), with the already-fixed outer checks \(W_D\) retained.
3. For every newly fixed Z vector, use symplectic Gram–Schmidt on \(G_0\) to identify its X-type conjugate. Remove that conjugate from the freely variable gauge pairs, or reclassify it as a fixed logical/classical operator exactly as the rank calculation dictates.
4. Recompute \(S_F,G_F,L_F\), where \(S_F\) is the enlarged fixed stabilizer, \(G_F\) is generated by the remaining gauge pairs together with \(S_F\), and \(L_F\) contains only label operators commuting with \(S_F\) and not identified with a gauge or logical operator.
5. Reject the profile if \(S_F\) is not isotropic, if \(S_F\not\subseteq G_F\), if the claimed label operators are not mutually compatible, or if the marker check space has a nontrivial label-dependent syndrome collision.

This is an explicit finite linear-algebra operation. It may reduce \(m\) or \(r\); that reduction must be reported rather than hidden in a nominal parameter formula.

### F.6 Hybrid-subsystem parameters

A binary Pauli matrix is represented in symplectic form as \([A_X\mid A_Z]\). For a proposed sector, the implementation will compute:

* \(s=\operatorname{rank}(S)\), the independent stabilizer rank;
* \(g=\operatorname{rank}(G)\), the independent gauge-group rank;
* \(r=(g-s)/2\), provided the gauge-group commutator rank verifies this subsystem interpretation;
* \(k=n-s-r\), the logical-qubit count per classical sector; and
* \(m\) from the rank difference between the common outer sector and the orthogonal inner sectors, equivalently by enumerating the independent classical-label eigenvalue choices.

For a clean hybrid-subsystem decomposition, the target relation is

\[
\dim(\text{direct-sum code})=2^{k+r}\,2^m,
\]

with the label operators and their conjugates explicitly identified. Closed formulas in terms of \(k_X,k_Z,\dim D_X,\dim D_Z\) will be stated only after the symplectic-rank derivation succeeds.

### F.7 Candidate dressed distances

The four-code CSS theorem from the latest source suggests the following pre-proof targets:

\[
 d_X^\star=\min\operatorname{wt}
 \left((D_X+D_Z^\perp)\setminus C_Z^\perp\right),
\]
\[
 d_Z^\star=\min\operatorname{wt}
 \left((D_Z+D_X^\perp)\setminus C_X^\perp\right).
\]

The actual synchronizable hybrid-subsystem distances may be smaller after marker gauge fixing. The implementation must compute both the pre-proof target and the final stabilizer/gauge coset distance. The paper must report the latter.

## G. Construction

### G.1 Classical-code selection

1. Choose \(n\) and four cyclic code defining sets.
2. Build \(C_X,C_Z,D_X,D_Z\) and generator/parity-check matrices.
3. Verify all inclusions and dual-containment/commutation conditions by exact binary linear algebra.
4. Choose a marker vector \(b_X\), initially the coefficient vector of \(g_{D_X}(x)\), and verify \(b_X\notin C_X\).
5. Compute \(f_X\), its factorization, and \(\operatorname{ord}(f_X)\).

### G.2 Initial hybrid-subsystem code

1. Construct the asymmetric inner CSS stabilizer from \(C_X,C_Z\).
2. Construct the outer gauge/label structure from \(D_X,D_Z\) using the general CSS hybrid-subsystem rank construction in the 2024 source.
3. Compute a symplectic hyperbolic basis independently of the arbitrary input generator basis.
4. Apply the marker-compatible gauge-fixing profile that makes \(M_X\) fixed.
5. Identify the logical-qubit, gauge-qubit, and classical-label pairs. Reject the tuple if any claimed sector has rank zero or if the commutation table is inconsistent.

### G.3 Marker and block extension

For each allowed classical label, apply the X-type marker \(X(b_X)\) (or a verified marker representative in the same sector), attach \(a_l\) left and \(a_r\) right ancillas in \(|0\rangle\), and apply the same cyclic boundary CNOT extension used in the inherited QSC construction.

The marker must not be counted as an extra classical bit unless the synchronization requirement is intentionally sacrificed and the loss is reported. If multiple marker-compatible vectors are possible, the deterministic selection rule is the lexicographically first one with maximum verified order.

### G.4 Receiver procedure

For a received block with an unknown displacement \(\alpha\in[-a_l,a_r]\):

1. select the current n-qubit window;
2. correct X-type errors on that window with the verified outer X-sector decoder;
3. measure the fixed marker-check space \(M_X\) and decode \(\alpha\) from the syndrome;
4. realign the block;
5. correct X- and Z-type errors on the realigned block using the verified dressed-distance decoders;
6. remove the marker and undo the extension; and
7. decode the quantum, gauge, and classical sectors according to the chosen hybrid-subsystem profile.

The proof and simulator must enforce the source assumption that every n-qubit window has no more X errors than the outer X decoder can correct. Z errors are counted over the full received block according to the selected distance guarantee.

## H. Theorem and proposition targets

Every item below is a **target**, not an established theorem.

### Target H1: four-code marker theorem

Under package (P), an explicit marker-compatible gauge-fixing rank condition, and a verified injectivity condition, prove existence of an \((a_l,a_r)\)-synchronizable hybrid-subsystem CSS code of length \(N=n+a_l+a_r\). Its logical, classical, and gauge dimensions must be given by symplectic ranks, and its X/Z correction guarantees must be the final dressed coset distances.

### Target H2: cyclic injectivity lemma

For a cyclic marker representative \(b_X\) and quotient \(f_X=g_{C_X}/g_{D_X}\), prove that the marker syndrome is represented by a function of \(x^\alpha\bmod f_X(x)\). Establish a sufficient condition

\[
 a_l+a_r<\operatorname{ord}(f_X)
\]

for all allowed shifts to yield distinct syndromes, including negative shifts and all permitted label sectors.

If the four-code gauge profile changes the check space, prove the corresponding condition for \(M_X\) rather than assuming the common-pair lemma.

### Target H3: asymmetric distance proposition

Derive the dressed X/Z distance expressions after gauge fixing. Determine when the pre-proof quantities \(d_X^\star,d_Z^\star\) equal the final distances and when they are only lower bounds.

### Target H4: BCH instantiation theorem

For a stated family of primitive binary BCH defining sets, prove:

* all four inclusions and dual-containment conditions;
* the code dimensions from cyclotomic cosets;
* the exact or explicitly certified classical/coset distances under the 2025 conditions or an independent proof; and
* \(\operatorname{ord}(f_X)=n\) whenever the selected quotient contains a primitive factor.

No infinite-family theorem is to be claimed until the index ranges and exceptional cosets have been checked symbolically.

### Target H5: symmetric-recovery proposition

When \(C_X=C_Z=C\) and \(D_X=D_Z=D\), prove that the construction reduces, up to stabilizer/gauge basis changes, to the relevant 2024 common-pair code and to the inherited QSC in the no-gauge/no-classical specialization. This is a regression result and also protects against a false novelty claim.

### Target H6: resource-profile proposition

For a fixed four-code tuple, characterize which complement dimensions can be allocated to marker checks, gauge pairs, and classical labels. If a generalized resource identity exists, state it only after deriving it from ranks and identify exactly which assumptions differ from the 2024 common-pair identity.

## I. Derivation and verification plan

### I.1 Classical algebra

* Use defining-set tests for cyclic inclusion and Euclidean dual containment.
* Independently divide generator polynomials and verify the quotient reconstructs \(g_{C_X}\).
* Compute polynomial orders by factor orders and by direct repeated multiplication modulo \(f_X\).
* Verify all dimensions by both generator-matrix rank and cyclotomic-coset counts.

### I.2 Symplectic construction

* Form the binary symplectic matrices for inner stabilizers, outer gauge generators, marker checks, label operators, and gauge-fixing operators.
* Check every claimed commutator with \(\Omega=\begin{bmatrix}0&I\\I&0\end{bmatrix}\).
* Verify \(S\subseteq G\), \(S\subseteq G^\perp\), and the expected commutator rank of \(G\).
* Compute \(k,m,r\) from ranks and compare them with any symbolic formulas.
* Test invariance under random changes of generator basis and hyperbolic basis.

### I.3 Marker proof

The proof must explicitly show the analogue of

\[
H_{C_X}O(b_X,-\alpha)^T
\]

for the actual fixed check space. The required steps are:

1. show that the preliminary X correction removes the window error without changing the marker label;
2. express each shifted marker as a cyclic polynomial shift;
3. divide by the outer marker generator and reduce modulo the quotient factor;
4. prove that equal remainders imply equal shifts in the allowed interval; and
5. prove that gauge and classical-label operators do not produce the same measured syndrome.

The last step is the part not supplied by the common-pair proof and is the principal mathematical risk.

### I.4 Pauli correction proof

After realignment, prove that the outer X decoder corrects the allowed window errors and that the final X/Z decoders correct the full-block errors up to the dressed distances. The proof must distinguish:

* a stabilizer error, which is harmless;
* a gauge error, which is harmless only within a subsystem sector;
* a classical-label-changing error, which is not harmless; and
* a logical error, which is not correctable.

### I.5 Small-instance exhaustive proof audit

For the smallest valid instances, enumerate all Pauli errors below the claimed weights and all allowed shifts. Directly verify the hybrid Knill–Laflamme condition sector by sector and verify that no two shift/label pairs have the same marker syndrome. These checks are independent of the symbolic proof and are not a substitute for it.

## J. Algorithms

### J.1 Deterministic code factory

Inputs: field \(\mathbb F_2\), length \(n\), four defining sets or generator polynomials, and a marker profile.

Outputs: generator/parity-check matrices, duals, inclusion certificates, dimensions, factor orders, symplectic matrices, rank profile, and a pass/fail reason.

Required operations:

* binary polynomial addition, multiplication, division, gcd, reciprocal, and factor handling;
* cyclotomic-coset generation;
* binary Gaussian elimination;
* cyclic shift and polynomial remainder;
* symplectic rank and commutation checks; and
* exact low-weight/coset-distance search.

The first implementation should use the Python standard library plus a small self-contained GF(2) module. SageMath and Magma may be used as independent validators, not as the only implementation.

### J.2 Four-code search

```text
for extension_degree mu in preregistered_range:
    n = 2^mu - 1
    build all allowed primitive BCH defining intervals
    for (C_Z, C_X, D_Z, D_X) in deterministic_order:
        if not verify_inclusions_and_dual_conditions(): continue
        for marker b_X in deterministic_marker_candidates:
            if b_X in C_X: continue
            compute f_X and ord(f_X)
            build marker-compatible gauge-fixing profile
            if symplectic_rank_or_commutation_test_fails(): continue
            compute k, m, r and final dressed d_X, d_Z
            if no_positive_quantum_or_hybrid_payload(): continue
            save certificate and candidate
return Pareto_frontier(candidates)
```

No random search is needed for the first paper. If a randomized hyperbolic-basis routine is used for exploration, the final certificate must be regenerated deterministically.

### J.3 Exact-distance modes

1. **Exhaustive mode:** enumerate all codewords when the dimension is below a fixed, recorded threshold.
2. **Meet-in-the-middle mode:** split generator rows and search for low-weight vectors for moderate dimensions.
3. **Certified BCH mode:** invoke only the explicit-distance conditions proved in the paper or in a cited source, with all hypotheses checked.
4. **Bound-only mode:** retain lower bounds for exploration but exclude those points from any “exact parameter” table.

### J.4 Shift-syndrome verifier

For every candidate and every \(\alpha\) in the requested interval:

1. build the shifted marker vector;
2. compute the syndrome using the actual measured check matrix;
3. compare all pairs \((\alpha,\text{classical label})\); and
4. record collisions, if any, with the responsible gauge or label operator.

The verifier must use both direct binary matrix multiplication and polynomial remainder arithmetic.

### J.5 Code-capacity simulator

Use an explicitly defined biased Pauli model, for example independent X and Z components with probabilities \(p_X,p_Z\), or a fully specified \(p_I,p_X,p_Y,p_Z\) model. State which model is used; do not call independent components a depolarizing channel.

For each trial:

1. sample a legal shift;
2. sample Pauli supports and enforce or record the window-weight condition;
3. run the syndrome/marker decoder;
4. check whether the residual lies in the allowed stabilizer/gauge group and preserves the classical label and logical state; and
5. record synchronization failure, X logical failure, Z logical failure, label failure, and total failure separately.

Gate and measurement faults are excluded from the central experiment and must be listed as a limitation.

## K. Parameter selection

### K.1 Primary family

Use primitive binary BCH codes of length

\[
 n=2^\mu-1,
\]

initially with \(\mu\in\{5,6,7,8,9\}\), subject to runtime and exact-distance certification. The dual-containing design-distance range will be taken from the published BCH criterion and independently checked for every tuple.

The pre-registered search order is:

1. maximize verified synchronization order \(S=\operatorname{ord}(f_X)\);
2. retain only positive logical-qubit and intended hybrid-subsystem payloads;
3. maximize the biased-channel-relevant distance pair \((d_Z,d_X)\) lexicographically for a declared \(p_Z/p_X\);
4. maximize \(k+m+r\) only after the previous filters; and
5. report the full Pareto frontier rather than a single cherry-picked point.

### K.2 BCH chain geometry

The first restricted search uses

\[
 C_Z\subseteq C_X\subseteq D_X,
 \qquad C_Z\subseteq D_Z\subseteq D_X,
\]

with defining distances ordered so that the larger designed distance gives the smaller code. The search will not assume that designed distance equals true distance; it will store the certificate type for each reported value.

A first unit-test target is a small tuple with four roles drawn from the \(n=31\) BCH chain, for example distinct or partially coincident design intervals in the order “high Z protection, intermediate X inner protection, intermediate outer Z protection, lower outer X protection.” This is a test target, not a claimed parameter set or result. It must pass all rank, order, and distance checks before appearing in any result table.

### K.3 Synchronization allowance

For each certified candidate, evaluate:

* the maximal total allowance \(S-1\);
* balanced splits \((\lfloor(S-1)/2\rfloor,\lceil(S-1)/2\rceil)\); and
* deliberately one-sided splits.

Do not compare only \(a_l+a_r\) if the decoder or physical application is directionally asymmetric.

### K.4 Excluded parameter claims

No numerical family, rate, distance, or improvement is promised in advance. If only lower bounds can be certified, the manuscript must label them as lower bounds. If the four-code rank profile produces no hybrid-subsystem payload for the BCH range, the direction fails its feasibility gate rather than being padded with unverified examples.

## L. Validation and independent cross-checks

### L.1 Algebraic checks

* generator divisibility and code inclusion;
* dual containment by reciprocal generator and by matrix orthogonality;
* dimensions by two independent rank methods;
* order by factor lcm and direct modular powering;
* marker-syndrome injectivity by two implementations; and
* dressed-distance computation by direct coset search for small instances.

### L.2 Symmetric regression tests

Set \(C_X=C_Z=C\) and \(D_X=D_Z=D\). Recover the common-pair QSC and the appropriate 2024 subsystem/hybrid-subsystem parameter profile. A failure here blocks all asymmetric claims.

### L.3 Exhaustive quantum cross-check

For small \(n\), construct the full stabilizer/gauge groups and test all Pauli errors through the claimed X/Z weights. For each allowed shift, verify that the decoder returns the correct boundary and that the residual is an allowed stabilizer or gauge operator. Test every classical label for a hybrid code.

### L.4 Independent software cross-check

At least one of the following must reproduce the final certificates without importing the main implementation’s code:

* SageMath finite-field/cyclic-code routines;
* Magma cyclic-code and minimum-distance routines; or
* a second small plain-Python implementation written from the saved defining sets.

Published source examples should be reproduced first, including at least one explicit-distance BCH or Whiteman example, before the new search is trusted.

### L.5 Statistical simulation

Use fixed seeds, report the number of trials and confidence intervals, and separate synchronization, label, X-logical, Z-logical, and total failure. Simulation is evidence of operational behavior under the stated model, not a proof of the theorem.

### L.6 Go/no-go validation gate

The project proceeds to a manuscript only if it has:

1. a proved marker theorem or a rigorously characterized obstruction;
2. at least one nontrivial four-code rank profile with a positive intended payload;
3. an independently reproduced syndrome/order certificate;
4. exact or explicitly certified distances for all headline points; and
5. a comparison that is fair at fixed field, block length, payload constraints, and synchronization allowance.

## M. Reputable-literature benchmarks

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

## N. Expected tables and figures

### Tables

1. **Source audit:** construction type, field, length family, order proof, distance status, and limitation.
2. **Four-code certificates:** \((C_X,C_Z,D_X,D_Z)\), generator/defining sets, dimensions, dual checks, marker, \(\operatorname{ord}(f_X)\), and rank profile.
3. **Exact distance status:** \(d_X,d_Z\), proof/certificate method, and whether the value is exact or a lower bound.
4. **Resource profiles:** \((k,m,r,d_Z/d_X,S)\) for every Pareto point.
5. **Symmetric regression:** the same candidates with \(C_X=C_Z\) and \(D_X=D_Z\).
6. **Published benchmarks:** only comparable rows with citations and assumptions.
7. **Failure ledger:** rejected tuples and the exact failed condition, especially syndrome collisions and nonpositive ranks.
8. **Simulation:** channel parameters, trials, confidence intervals, and separate failure modes.

### Figures

1. Four-code inclusion lattice and marker/gauge-fixed subspaces.
2. Symplectic commutation diagram showing inner stabilizer, outer gauge, marker checks, and classical labels.
3. Shift-syndrome points \(\alpha\mapsto\sigma_\alpha\) and any collision boundary.
4. Pareto frontier in \((d_Z,d_X,k+m+r,S)\) space.
5. Logical/label/synchronization failure rates versus biased noise.
6. Decoder flow: window X correction → marker syndrome → realignment → full CSS/hybrid-subsystem correction.

## O. Reproducibility

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

## P. Risks and OPEN items

### Mathematical risks

1. **Marker checks may be gauge operators rather than fixed stabilizers.** The proposed gauge-fixing profile may consume too much payload or may not commute with all classical labels.
2. **The four-code quotient may not control the actual syndrome.** The correct quotient could involve an intersection or a restricted marker-check space rather than \(g_{C_X}/g_{D_X}\).
3. **Outer correction may not use the raw distance of \(D_X\).** Final distances must be dressed coset distances after gauge fixing.
4. **Positive hybrid-subsystem ranks may be rare.** If all small BCH tuples collapse to a stabilizer core or a zero-payload code, the proposed family is not computationally feasible as stated.
5. **The common-pair specialization may fail under a careless basis choice.** Any such failure is an implementation/proof error until independently resolved.

### Literature and evidence OPEN items

1. **Final 2026 source text:** obtain and diff the IEEE TQE version, DOI 10.1109/TQE.2026.3673092, against local `2409.11312v2.pdf`; update theorem numbering and publication metadata.
2. **External novelty sweep:** search IEEE Xplore, Web of Science, Scopus, MathSciNet, zbMATH, Crossref, arXiv, and Google Scholar for the exact four-code/asymmetric/synchronizable/hybrid-subsystem intersection. The current web search is preliminary and is not an absence proof.
3. **Prior asymmetric QSC claims:** check books, theses, conference proceedings, and non-English indexing for phrases such as “asymmetric quantum synchronizable code,” “asymmetric QSC,” “synchronizable asymmetric CSS,” and “asymmetric hybrid subsystem synchronization.”
4. **Author artifacts:** no source code or datasets were found in the repository. Verify whether the 2023/2025 Magma checks or code tables have public supplementary files; if not, reproduce them independently.
5. **Journal status:** verify current SCIE indexing, JCR quartile, and top-10-percentile status of the target venue at submission time rather than relying on a static claim.

### Scope risks explicitly excluded

* fault-tolerant syndrome extraction;
* gate/measurement noise;
* qudit generalization;
* repeated-root/QC replacement of the BCH family;
* deletion/loss synchronization; and
* an unproved universal resource optimality theorem.

If any excluded topic becomes necessary for the proof, stop and re-scope rather than silently enlarging the paper.

## Q. Target journal class

**Primary target:** *IEEE Transactions on Information Theory* or an equivalently selective, SCIE-indexed top coding/information-theory journal. The paper must meet a Q1/top-10%-quartile standard at the time of submission, with a theorem-level contribution, independently reproducible computations, and fair published benchmarks.

**Secondary fit, only if the hybrid-subsystem interpretation has clear quantum-information significance:** *Physical Review A* or a comparably selective quantum-information journal. The journal choice must be rechecked using current JCR/Scimago/Web of Science records; no quartile claim is made in this blueprint.

The 2026 *IEEE Transactions on Quantum Engineering* version of the source paper is an essential benchmark and possible venue context, but the proposed paper should not target it merely because it extends that source; the expected contribution should be judged against the stronger coding-theory standard.

## R. Manuscript architecture

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

## S. Explicit nontrivial novelty test

A novelty claim is allowed only if all five gates pass.

### S1. Publication-level literature gate

Before drafting the abstract, run and archive searches across the databases in Section P using at least:

* `"asymmetric quantum synchronizable"`;
* `"asymmetric" AND "quantum synchronizable code"`;
* `"synchronizable" AND "hybrid subsystem" AND CSS`;
* `"synchronizable" AND "asymmetric CSS"`;
* `"quantum synchronizable" AND (C_X OR C_Z OR four codes)`; and
* equivalent searches for `misalignment`, `block synchronization`, `gauge fixing`, `hybrid stabilizer`, and `subsystem`.

Read any exact or near-exact hit, including dissertations and conference papers. A preliminary search found the common-pair 2024/2026 hybrid-subsystem paper and ordinary asymmetric-QECC literature, but that is not sufficient for an absence claim.

### S2. Containment gate

Implement a source-reproduction map. The proposed construction fails novelty if every candidate can be reduced by any combination of:

* setting \(C_X=C_Z\) and \(D_X=D_Z\);
* swapping X and Z labels;
* changing only a generator or hyperbolic basis;
* relabeling a common-pair gauge/classical sector; or
* applying an already published QC/ring/constacyclic map without a new marker proof.

### S3. Structural gate

At least one headline candidate must satisfy all of:

\[
 C_X\ne C_Z,\qquad D_X\ne D_Z\ \text{or a provably asymmetric marker profile},
\]

with a nonzero quantum payload and a nonzero intended hybrid-subsystem payload. It must have independently verified X/Z dressed distances that are not forced equal by the common-pair specialization.

### S4. Strict comparison gate

At fixed field, physical length, synchronization allowance, and comparable payload, the new point must show a strict improvement in at least one meaningful quantity—such as a protected distance in the biased sector, quantum/classical/gauge payload, or verified order—without being worse in every other reported quantity. If only a different parameter tradeoff exists, report it as a tradeoff, not as “better.”

### S5. Proof and implementation gate

The marker theorem, rank/distance definitions, source regression, independent implementation, and exhaustive small-instance checks must all pass. A parameter table without the four-code synchronization proof is not a novelty result.

**Decision rule:** if S1–S5 do not all pass, the manuscript must state “candidate direction rejected or unresolved” and must not claim a new asymmetric synchronizable hybrid-subsystem code.

---

# Final five-component summary

1. **Research question:** Can separate X/Z cyclic code pairs retain a unique quantum synchronization marker after the 2024 hybrid-subsystem gauge construction?
2. **Mathematical contribution sought:** A four-code, marker-compatible synchronizable hybrid-subsystem CSS theorem with rank-defined \((k,m,r)\), dressed \((d_Z,d_X)\), and order-based synchronization guarantees.
3. **Construction and computation:** Primitive binary BCH four-code tuples, exact inclusion/order/rank checks, certified or exact coset distances, deterministic Pareto search, and code-capacity decoding simulation.
4. **Validation standard:** Symmetric-source regression, independent polynomial and symplectic implementations, exhaustive small-instance Pauli/shift checks, published QSC/AQECC benchmarks, and an archived external novelty search.
5. **Go/no-go and publication target:** Proceed only if the marker proof, positive nontrivial ranks, certified distances, independent checks, and S1–S5 novelty gates pass; target a Q1/top-10%-standard coding/information-theory journal, with current indexing verified at submission.

# Complete A–S execution checklist

| Section | Required deliverable before manuscript drafting |
|---|---|
| A | Final title that still accurately describes the proved object. |
| B | Literature-supported gap and one central question. |
| C | Source-by-source inherited/extended/new ledger. |
| D | One theorem-level contribution, not a cosmetic parameter change. |
| E | Falsifiable hypotheses and rejection criteria. |
| F | Exact four-code, marker, rank, distance, and noise definitions. |
| G | Encoder, marker, gauge-fixing, extension, and decoder specification. |
| H | Proved-or-rejected theorem/proposition targets. |
| I | Algebraic, symplectic, marker, distance, and edge-case derivations. |
| J | Deterministic code factory, search, order, distance, decoder, and simulator algorithms. |
| K | Preregistered BCH ranges, filters, and Pareto selection rules. |
| L | Independent checks, exhaustive small cases, regressions, and confidence reporting. |
| M | Fair reputable-literature benchmark table. |
| N | Parameter/resource/failure tables and syndrome/Pareto/decoder figures. |
| O | Versioned environment, inputs, seeds, certificates, and regeneration commands. |
| P | Risks, exact OPEN sources, and a documented go/no-go decision. |
| Q | Current SCIE/JCR/top-10-percentile verification for the target journal. |
| R | Manuscript sections with inherited, target, and proved-result labels. |
| S | Completed five-gate nontrivial novelty test with an archived search record. |
