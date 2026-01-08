# Evaluation: P2626R0 — charN_t incremental adoption: Casting pointers of UTF character types

**Paper:** P2626R0  
**Title:** charN_t incremental adoption: Casting pointers of UTF character types  
**Authors:** Corentin Jabot  
**Link:** [https://wg21.link/P2626R0](https://wg21.link/P2626R0)  
**Revision Date:** 2022-08-09  
**Evaluation Date:** 2026-01-08

---

## Gate: Standardization Justification

**G0. What coordination failure does this solve?** ✅ PASS  
The standard created a coordination failure by introducing `char8_t`/`char16_t`/`char32_t` (C++11/C++20) without providing migration tools. Paper documents that Win32 uses `wchar_t*` for UTF-16, iconv/QString expect `char*`, and there is currently **no way** to interoperate without UB or O(n) copies.

**G1. Why not third-party?** ✅ PASS  
Paper explicitly states these functions "require some compiler support in the form of a magic built-in" for constexpr lifetime management. A third-party library cannot implement this without invoking undefined behavior.

**G2. Perpetual costs acknowledged?** ⚠️ PARTIAL  
Paper acknowledges compiler support is required but does not explicitly analyze implementation burden across vendors, interaction surface with existing library, or maintenance commitment.

**Gate Result:** ✅ PROCEED TO EVALUATION — Standardization justified due to language integration requirement

---

🟡 CONCERNS: Well-justified proposal requiring compiler support, but lacks economic analysis and retrospective commitment.

| Category | Score | |
|----------|-------|---|
| 1. Use-Case Validation | 2 | ✅ |
| 2. Economic Analysis | 0 | ❌ |
| 3. Vocabulary Necessity | 1 | ⚠️ |
| 4. External Validation | 1 | ⚠️ |
| 5. Implementation | 1 | ⚠️ |
| 6. Completeness | 2 | ✅ |
| 7. Incentive Alignment | 1 | ⚠️ |
| 8. Retrospective Commitment | 0 | ❌ |
| 9. Process & Timeline | 1 | ⚠️ |
| 10. Practical Usability | 2 | ✅ |
| 11. Safety & Stability | 1 | ⚠️ |
| 12. Ecosystem Consideration | 2 | ✅ |
| 13. Expert Weighting | 2 | ✅ |
| **TOTAL** | **16/26** | Library threshold: 14 ✅ |

## Summary Exposition

P2626R0 addresses a genuine gap in the C++ standard: the inability to safely interoperate between the UTF character types (`char8_t`, `char16_t`, `char32_t`) introduced in C++11/C++20 and existing codebases that use `char`, `wchar_t`, or unsigned integer types. The Tony table brilliantly demonstrates that all current approaches are either ill-formed, undefined behavior, or require O(n) operations. The proposed `cast_as_utf_unchecked` and `cast_utf_to` functions provide a clean, constexpr, well-defined solution.

The proposal's strongest aspect is its clear justification for standardization: these functions require compiler magic to provide constexpr lifetime management semantics. A third-party library simply cannot implement this functionality correctly. The paper also cites concrete existing practices (Win32, iconv, QString, ICU) showing real-world interoperability needs.

Key weaknesses include the absence of economic analysis (perpetual implementation costs), no retrospective commitment, and limited field experience with the prototype. The "crude" Clang prototype demonstrates feasibility but hasn't gathered independent user feedback. For a library-only proposal, it passes the threshold, but strengthening economic justification and adding success criteria would improve confidence.

## Red Flags Identified

🚩 No retrospective plan — No success criteria or post-adoption review defined

🚩 Economic analysis missing — No discussion of implementation burden across vendors or ongoing maintenance costs

🚩 Limited field experience — Prototype described as "crude" and "probably not entirely correct"; no independent user validation

---

## Category-by-Category Analysis

### 1. Use-Case Validation — ✅

**Score: 2/2**

The paper opens with an excellent "Tony table" showing seven problematic attempts to convert between `wchar_t*` and `char16_t*` (ill-formed static_cast, UB reinterpret_cast, O(n) transforms, non-constexpr lifetime management) versus the clean one-liner solution. This is textbook use-case-driven design where the motivating example demonstrates exactly why the feature is needed.

**Evidence cited:** "The innocent: ill-formed... The 10x developer: UB... The expert: not constexpr" — systematic demonstration of current inadequacy.

### 2. Economic Analysis — ❌

**Score: 0/2**

The paper does not quantify standardization costs. There is no discussion of implementation burden across compiler vendors, no estimate of interaction surface with existing library components, and no acknowledgment of perpetual maintenance requirements. The paper treats "useful" and "currently impossible without UB" as sufficient justification without economic analysis.

**Evidence cited:** None found. The closest is "they do require some compiler support in the form of a magic built-in" but no cost quantification.

### 3. Vocabulary Necessity — ⚠️

**Score: 1/2**

The paper documents real interoperability problems: Win32 uses `wchar_t*` for UTF-16 data, iconv/QString expect `char*` for UTF-8, ICU uses either `char16_t` or `uint16_t`. These are concrete cases where type boundaries prevent clean interoperation. However, there are no bug reports cited, no quantified harm (hours wasted, bugs shipped), and no specific projects documented as failing to interoperate.

**Evidence cited:** "Many Win32 functions deal in wchar_t* pointers, but the encoding is UTF-16, so it should be possible to exchange char16_t* with these interfaces, but isn't."

### 4. External Validation — ⚠️

**Score: 1/2**

The paper mentions Microsoft (Win32), Qt (QString), ICU, and iconv as ecosystems where this would be useful, but does not cite specific organizations requesting this feature or provide testimonials from production deployments. The acknowledgments reference "many people who voiced their desire for better usability of the charN_t types" without naming them.

**Evidence cited:** "The many people who voiced their desire for better usability of the charN_t types" — too vague to count as named users.

### 5. Implementation & Field Experience — ⚠️

**Score: 1/2**

A Clang prototype exists on Compiler Explorer demonstrating constexpr usage and iconv integration. However, the author describes it as "crude" and "probably not entirely correct" due to lack of `start_lifetime_as_array` support. No field experience beyond the prototype is documented, and no independent users have validated the design.

**Evidence cited:** "I prototyped a crude implementation in clang, but in the absence of existing support for std::start_lifetime_as_array, the implementation is probably not entirely correct."

### 6. Completeness — ✅

**Score: 2/2**

The proposal is comprehensive: pointer overloads in `<utility>`, `span` overloads in `<span>`, `basic_string_view` overloads in `<string_view>`, and a feature test macro. Users can immediately use this with their preferred vocabulary type without additional scaffolding or ecosystem support.

**Evidence cited:** Complete wording provided for all three headers with full constraint and effect specifications.

### 7. Incentive Alignment — ⚠️

**Score: 1/2**

Corentin Jabot is a known and respected SG-16 contributor with clear expertise in Unicode/text handling. Corporate interests are not apparent. However, there is no explicit stewardship commitment post-acceptance, no succession plan, and no statement of who will maintain the feature long-term.

**Evidence cited:** Author is SG-16 domain expert; no explicit maintenance commitment found.

### 8. Retrospective Commitment — ❌

**Score: 0/2**

The paper defines no success criteria, no adoption targets, no mechanisms for gathering usage data, and no retrospective analysis plan. This is a "ship and forget" pattern where there is no way to evaluate whether the feature achieved its goals.

**Evidence cited:** None found.

### 9. Process & Timeline — ⚠️

**Score: 1/2**

As an R0 paper, no milestones are defined yet. The paper has a single author providing clear design authority. Non-goals are partially stated: single code units are deferred to `std::bit_cast`, validating variant is explicitly future work. However, there's no timeline for resolution and no explicit prioritization of use cases.

**Evidence cited:** "Why only supporting ranges of code units and not individual code units? std::bit_cast is perfectly suitable for that purpose."

### 10. Practical Usability — ✅

**Score: 2/2**

The Tony table conclusively demonstrates massive simplification. Seven broken or suboptimal approaches (ill-formed, UB, O(n), non-constexpr) are replaced by a single clean constexpr line. The API is intuitive: `cast_as_utf_unchecked` goes toward UTF types, `cast_utf_to<T>` goes away from them. The naming explicitly signals the unchecked/dangerous nature of the operation.

**Evidence cited:** Before/After comparison shows `const char16_t* u = ...` attempts all failing vs. `constexpr std::u16_string_view v = std::cast_as_utf_unchecked(L"Hello"sv);` succeeding.

### 11. Safety & Stability — ⚠️

**Score: 1/2**

The "unchecked" suffix appropriately signals that the function has preconditions (data must be valid UTF). The paper leaves room for a future `cast_as_utf` validating variant. However, there is no explicit safety roadmap discussion, no ABI analysis (though functions have minimal ABI concerns), and the constexpr requirement implicitly freezes certain implementation choices.

**Evidence cited:** "Leaving the room for a different function which does check for the validity of the UTF sequence and return an std::expected for example."

### 12. Ecosystem Consideration — ✅

**Score: 2/2**

The paper provides a compelling argument for standardization: these functions require compiler magic for constexpr lifetime management. A third-party library cannot implement this without UB. ICU's cast functions are cited as existing practice and inspiration. The proposal addresses a genuine capability gap, not mere convenience.

**Evidence cited:** "These functions have semantics somewhat similar to std::start_lifetime_as_array... They are also, unlike std::start_lifetime_as_array, constexpr. As such, they do require some compiler support in the form of a magic built-in."

### 13. Expert Weighting — ✅

**Score: 2/2**

The paper builds on P2590R2 (`start_lifetime_as`) from Timur Doumler and Richard Smith. Acknowledgments include Tom Honermann (SG-16 chair), Hubert Tong, Richard Smith, and David Goldblatt — recognized experts in language semantics and aliasing. ICU's existing cast functions inform the design. The author himself is an SG-16 domain expert.

**Evidence cited:** "Tom Honermann, Hubert Tong, Richard Smith, David Goldblatt for helping me have a better grasp on TBAA."

---

## Recommendations

1. **Add economic analysis**: Estimate implementation complexity for Clang, GCC, MSVC. Identify which existing built-ins can be leveraged.

2. **Define success criteria**: What adoption level would indicate this was worthwhile? How will usage be measured?

3. **Gather field experience**: Improve the Clang prototype and solicit feedback from projects currently struggling with charN_t interop (Qt, Windows-targeting codebases).

4. **Document specific harm**: Cite GitHub issues or bug reports where the lack of this facility caused real problems. "Should be possible but isn't" is weaker than "caused bug #12345."
