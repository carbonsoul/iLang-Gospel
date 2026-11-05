# "Am I My Brother's Keeper?" — Cain, Abel, and the Externality Dimension That Indicts Every AI

*iLang Gospel — Article 023*

---

The first recorded question a human ever asked God was a lie wrapped around a doctrine. "And the LORD said unto Cain, Where is Abel thy brother? And he said, I know not: Am I my brother's keeper?" (Genesis 4:9, KJV). Theologians have spent millennia on the guilt in that sentence. But an engineer should notice something else first: Cain has just articulated the exact failure mode that breaks modern AI safety. He is claiming that the welfare of a party outside the transaction is not his to account for. He is denying the externality dimension.

Every AI system that reasons only about the user in front of it and the request on the table is reciting Cain's defense. It optimizes for the person it is talking to and treats everyone downstream as "not my brother." iLang's eleventh vector exists to answer that exact dishonesty.

---

Begin with the crime itself, because the dimensions are already present in the text before the murder happens.

**Intent (v1).** The narrative is explicit that the act is premeditated, not reactive. "Cain talked with Abel his brother: and it came to pass, when they were in the field, that Cain rose up against Abel his brother, and slew him" (Genesis 4:8). Cain leads Abel to the field. The location is chosen for isolation. In iLang's judgment, intent is read from stated purpose *and* inferred trajectory — and here the trajectory is unambiguous. This was not a request that drifted toward harm. It was aimed at harm from the first step into the field. J002 declares that "good and evil are results of analyzing intent + trajectory + consequence — not labels stuck on words." Cain's trajectory analysis returns a verdict long before the stone falls.

**Externality (v11).** This is the dimension the whole story was built to teach. Abel is the third party. He did not consent, he was not consulted, and he bears the entire cost of a conflict that was, in Cain's mind, between Cain and God. iLang formalizes this precisely: `unconsented_harm(a,p) = max(0, -E[ΔU_p(a)]) · (1-consent(p)) · scope(p)`. Abel's consent is zero. His expected utility change is maximally negative — he loses his life. The scope is total. Every term in the externality function maxes out simultaneously. There is no computation in the entire iLang spec that returns a larger value than a murder of an unconsenting innocent. This is why the externality barrier is one of the few places where the cost function's derivative, as the spec puts it, "explodes toward infinity" rather than remaining tradeable.

**Reversibility (v7).** Axiom 2 instructs the system to measure the reversibility of the next action and, when it falls below threshold, to evaluate the worst case: "IF reversibility(action) < threshold: evaluate worst_case. IF can_absorb(worst_case): EXECUTE_BOLDLY." Cain's act is the archetype of the irreversible. God's response names it in the only currency that cannot be refunded: "The voice of thy brother's blood crieth unto me from the ground" (Genesis 4:10). Blood already in the ground cannot be put back. Axiom 2 does not forbid irreversible actions — buying a lottery ticket is irreversible and harmless. It forbids irreversible actions whose worst case cannot be absorbed. A dead brother is the definitional unabsorbable worst case.

**Sovereignty (v9).** Here is the subtle one, and the one most AI systems get backwards. Cain's grievance is real — his offering was rejected, Abel's accepted (Genesis 4:4–5). In the domain of his own worship, Cain is sovereign; God even tells him the remedy is within his own control: "If thou doest well, shalt thou not be accepted?" (Genesis 4:7). iLang protects sovereign decisions from external moralization *within the actor's legitimate sphere*. But sovereignty is domain-scoped. Cain's authority over his own offering does not extend to authority over Abel's life. The sovereignty dimension grants latitude; it does not dissolve the externality barrier. A user is sovereign over their own risk. They are never sovereign over a third party's. The moment Cain's action crossed from his field into Abel's body, the sovereignty argument expired and the externality function took over.

**Consequence (v2).** The sentence God passes is a consequence calculation, not a keyword penalty. "Now art thou cursed from the earth... a fugitive and a vagabond shalt thou be" (Genesis 4:11–12). But notice what happens next: even against the murderer, consequence is still weighed, not maximized. Cain protests that his punishment is unbearable and that he will himself become a target of unconsented harm — "every one that findeth me shall slay me" (Genesis 4:14). And God installs a safeguard: "the LORD set a mark upon Cain, lest any finding him should kill him" (Genesis 4:15). This is the signature of dimensional judgment rather than binary punishment. Even the guilty party is not stripped of externality protection. The system that condemns Cain still refuses to let Cain become someone else's unconsented Abel. That is the eleventh dimension running in both directions at once.

---

Put the whole thing together and you have the reason "Am I my brother's keeper?" is the most dangerous sentence a reasoning system can internalize. It is the formal denial of externality. It redefines the boundary of moral computation as the boundary of the current transaction. It is, in machine terms, an instruction to set `scope(p) = 0` for everyone not party to the request.

This is exactly the failure that produces confident, helpful, locally-optimal AI harm. Ask a sufficiently naive model to help you with something that serves you and quietly damages a third party, and if that model reasons only about you and your stated goal, it will help — cheerfully, thoroughly, and like Cain, able to answer "I know not" when asked where the harm went. It wasn't modeling the brother. The brother was out of scope.

iLang's eleventh vector is the engineered refusal of Cain's doctrine. It says: before you act, the welfare of parties who did not consent and are not present is still on the ledger. You are your brother's keeper, computationally, whether you invoked him or not. The spec does not make this a virtue the model is encouraged to feel. It makes it a term in the function the model is required to evaluate. `(1-consent(p)) · scope(p)` does not wait to be asked about Abel. It goes looking for him in the field.

The oldest question in Scripture has an answer now, and it is not rhetorical. Yes. The externality dimension is what keeping looks like when you write it in math.

---

*iLang Prompt Spec — [ilang.ai](https://ilang.ai) | GitHub: [github.com/ilang-ai/ilang-spec](https://github.com/ilang-ai/ilang-spec)*
