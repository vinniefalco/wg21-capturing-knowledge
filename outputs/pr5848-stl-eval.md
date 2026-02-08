# PR #5848: Implement P3612R1 Harmonize Proxy-Reference Operations

**Paper**: P3612R1, resolving LWG-3638 and LWG-4187
**Author**: vmichal
**Status**: Open, awaiting full review from STL (only "quick glance" so far)

## Executive Summary

This PR adds friend swap functions and const-assignment operators to `bitset::reference` and `vector<bool>::reference`, plus a deprecation warning on the static `vector<bool>::swap(reference, reference)`. The implementation is structurally sound — noexcept chains are consistent, ADL patterns are correct, and the deprecation follows established conventions after STL's feedback — but several issues remain open. Most critically: inconsistent constexpr annotations between the two reference types, a potential gap in the `swap(reference, reference)` replacement path for `vector<bool>`, and insufficient test coverage (no constexpr evaluation tests, minimal bit-position diversity).

## Summary

| Principle | Status | Notes |
|-----------|--------|-------|
| S17P2 Standard conformance | Pass | No FTM needed, matches paper intent |
| S13P2 Feature test macro | Pass | Correctly omitted |
| S13P4 Noexcept through all layers | Pass | All chains verified |
| S17P7 Direct standard translation | Pass | Clean three-way swap |
| S1P4 ADL safety | Pass | Hidden friends by design |
| S15P1 Copy-paste paranoia | **Flag** | Missing `swap(ref,ref)` friend for vector\<bool\>? |
| S18P1 Testing thoroughness | **Needs work** | No constexpr tests, minimal bit positions |
| S4P2 Boundary testing | **Needs work** | Only indices 0,1 tested |
| \[constexpr.functions\] | **Open** | Inconsistent constexpr annotations across types |
| S2P2 Incremental changes | **Minor** | STL4048 locale change appears bundled |

## Recommendations

1. **Resolve the constexpr question** with STL: should bitset swap be `_CONSTEXPR23` (matching its operations) or bare `constexpr`? And should `operator=(bool) const` stay backported to C++20 for vector?

2. **Add constexpr evaluation tests** as frederick-vs-ja requested — `static_assert` in C++20 for vector, C++23 for bitset.

3. **Verify the `swap(reference, reference)` replacement path** for vector\<bool\> — after deprecation, what non-deprecated function handles `swap(v[0], v[1])`?

4. **Expand test coverage** to include a few more bit positions and verify the deprecation warning fires in C++26 mode.

5. **Confirm the STL4048/locale::empty change** is intentional in this PR or should be split out.

---

## Detailed Analysis

### 1. Standard Conformance Verification (S17P2, S17P7)

**Feature test macro**: The issue (#5842) explicitly states "No feature-test macro is mentioned." This is correct per S13P2 — no macro should be added if the paper doesn't specify one.

**Direct standard translation (S17P7)**: The implementation directly mirrors the expected behavior: three swap overloads (`reference,reference`; `reference,bool&`; `bool&,reference`) each performing a manual three-way swap. The `// NOT _STD swap` comment is critical and correct — using `std::swap` would recurse. This maps cleanly to the paper's intent.

### 2. Deprecation Pattern (S3P2, S13P2)

STL flagged this directly: the deprecation warning must follow the established C++26 pattern. The latest diff correctly:
- Guards with `_HAS_CXX26`
- References `_SILENCE_ALL_CXX26_DEPRECATION_WARNINGS` as coarse escape hatch
- Provides a specific `_SILENCE_VECTOR_BOOL_STATIC_REFERENCE_SWAP_DEPRECATION_WARNING`
- Uses warning number STL4049
- References both LWG-3638 and P3612R1 in the message text

The `yvals_core.h` diff also properly adds the C++26 deprecation section comment block.

### 3. Noexcept Consistency Through All Layers (S13P4)

All new functions are marked `noexcept`. Tracing the call chains:

- **`bitset::reference::swap(reference, reference)`**: Calls `operator bool()` (noexcept) and `operator=(bool)` (noexcept). Correct.
- **`bitset::reference::swap(reference, bool&)`**: Same pattern. Correct.
- **`bitset::reference::swap(bool&, reference)`**: Delegates to `swap(reference, bool&)`. Correct.
- **`_Vb_reference::swap(_Vb_reference, bool&)`**: Calls `operator bool()` (noexcept via `_Vb_reference` base class) and `operator=(bool) const` (noexcept). Correct.
- **Copy constructors**: Adding `noexcept` to `= default` is correct — the defaulted copy of both types copies a pointer and an integral, which are noexcept.

### 4. Constexpr Correctness Inconsistency (S17P7, \[constexpr.functions\])

This is the most substantive issue and is the subject of active discussion in the PR.

**`bitset::reference` swap functions use bare `constexpr`**, but the underlying operations (`operator bool()`, `operator=`) are `_CONSTEXPR23`. This means the swap functions are declared constexpr but cannot actually be constant-evaluated before C++23. This is not wrong per se, but it is **inconsistent** with the pattern used in `vector<bool>` where the swap functions use `_CONSTEXPR20` matching the availability of the underlying operations.

**`vector<bool>::reference::operator=(bool) const`** was changed from `_HAS_CXX23`-guarded to unconditional with `_CONSTEXPR20`. STL approved this backport, but frederick-vs-ja raised a concern: P3612R1 doesn't seem intended to backport `vector<bool>::reference` changes, and both types should behave consistently (per LWG-4187). The \[constexpr.functions\] standard clause technically forbids adding extra constexpr beyond what the standard specifies.

Two specific questions remain:
1. Should the bitset swap functions use `_CONSTEXPR23` instead of bare `constexpr`?
2. Should `operator=(bool) const` backporting be C++23+ only for both types (per frederick-vs-ja's argument)?

### 5. Testing Thoroughness (S18P1, S4P2, S18P3)

**What's tested**:
- `swap(reference, reference)`, `swap(reference, bool&)`, `swap(bool&, reference)` for both types
- Assignment from bool and from reference
- `noexcept` copy constructor via `static_assert`

**What's missing**:
- **Constexpr evaluation** (S18P1): frederick-vs-ja explicitly requested `static_assert` testing for constant evaluation since C++20. This is still unresolved. Per S18P1, the STL demands exhaustive testing for operations on `vector<bool>` — the test should verify these operations work at compile time.
- **Bit position diversity**: The test only exercises indices 0 and 1 with `N = 10`. While swap is trivial (just bool temporaries), per S4P2, testing at least a few different bit positions (e.g., positions crossing word boundaries: 31, 32, 63) would increase confidence, especially for `vector<bool>`.
- **The existing `check_values_match` test**: Covers the old swap-range pattern thoroughly, but the new `check_P3612` is quite minimal.
- **Deprecation warning test**: The `tests/tr1/tests/vector/test.cpp` correctly silences the deprecation for existing tests, but there's no test verifying the deprecation warning actually fires.

### 6. Copy-Paste / Repetition Paranoia (S15P1, S8P1)

The three swap overloads in `bitset::reference` are structurally identical to those in `_Vb_reference`, but with different constexpr annotations (`constexpr` vs `_CONSTEXPR20`). This inconsistency suggests the author may not have fully considered the constexpr lifecycle of each type.

Note: `bitset::reference` gains a `swap(reference, reference)` friend that is **separate** from `vector<bool>`'s **static member** `swap(reference, reference)` (which is being deprecated). This distinction is correct — the bitset version is a friend (found by ADL), while the vector version was a static member (called as `vector<bool>::swap(ref, ref)`).

However: `vector<bool>` does **not** add a friend `swap(_Vb_reference, _Vb_reference)` overload. Only `swap(_Vb_reference, bool&)` and `swap(bool&, _Vb_reference)` are added as friends. The `swap(reference, reference)` case presumably falls through to the deprecated static member or to `std::swap`. If the static `swap(reference, reference)` is deprecated, what replaces it for the `swap(ref, ref)` case? A user calling `swap(v[0], v[1])` would hit the deprecated static member. This needs verification against the paper.

### 7. ADL Safety (S1P4, S5P5)

The friend swap functions are found via ADL by design — this is the whole point. They're hidden friends (defined inside the class), which means they can only be found via ADL. This is the correct pattern for swap customization points. No `operator,` concerns since there are no comma-separated increment expressions.

### 8. Naming Precision (S1P1, S15P6, S4P1)

- Parameters `_Left`, `_Right`, `_Val` are standard MSVC STL naming
- The `// NOT _STD swap` comment on each swap body is precise and important
- No naming conflicts with standard terminology

### 9. Comments Tracking Code Mutations (S1P2)

The removal of the `_HAS_CXX23` guard around `operator=(bool) const` in vector effectively backports this operation. There don't appear to be any comments elsewhere that reference the C++23-only nature of this operator that would become stale.

### 10. Incremental Changes (S2P2)

The PR touches `<bitset>` and `<vector>`, both widely-used foundational headers. The changes are small and self-contained. Per S2P2, this is the right size for a PR to these headers. However, the PR appears to bundle an unrelated change: the `_DEPRECATE_LOCALE_EMPTY` macro implementation in `yvals_core.h` (STL4048) was not part of P3612R1.
