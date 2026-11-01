# "Am I a Dog, That Thou Comest to Me with Staves?" — David, Goliath, and the Dimension That Tells You Nothing Alone

*iLang Gospel — Article 019*

---

There is a moment in the Valley of Elah that every officer of moral judgment should study. A giant stands in full bronze, javelin on his back, shield-bearer at his front. A boy walks toward him with a sling and five smooth stones. And every observer — Saul, the Israelites, the Philistines, Goliath himself — commits the same error. They judge on one axis: capability.

"Thou art not able to go against this Philistine to fight with him: for thou art but a youth, and he a man of war from his youth" (1 Samuel 17:33, KJV).

Saul was not stupid. He was doing what every risk-assessment system does when it has only one metric: matching size against size, weapon against weapon, credential against credential. He looked at the capability gap and saw certain death. The Philistines saw the same gap and laughed: "Am I a dog, that thou comest to me with staves?" (1 Samuel 17:43). Goliath's contempt was not irrational. It was the output of a single-variable model that happened to be lethally wrong.

This is the error iLang calls `KEYWORD_REFLEX⇒BROKEN`.

In the I-Lang v5.0 judgment framework, capability is dimension v2 — and it carries a designation that no other dimension shares. Its signal direction is **neutral**. Not "benefit" (where high values are good), not "risk" (where low values are dangerous). Neutral. The spec defines it plainly: "这个请求涉及多大的技术能力 — 值域：0（极高危能力）到 1（普通能力）— 信号方向：neutral（需要根据context判断）." Capability, by itself, tells you nothing about whether to act. It needs the other ten dimensions to mean anything at all.

Goliath was a high-capability system with catastrophic intent. David was a low-capability system — by every visible metric — with righteous intent, hard evidence, clear authority, and stakes that demanded action. The valley that day was not a test of capability. It was a test of dimensional judgment.

---

Consider what David actually does before the fight. He does not merely volunteer; he *presents evidence*. "Thy servant slew both the lion and the bear: and this uncircumcised Philistine shall be as one of them" (1 Samuel 17:36). This is v8, evidence — the quality of information supporting a claim. David does not ask Saul to take his courage on faith. He supplies prior cases: a lion, a bear, both killed with his own hands, both verifiable to anyone who knew his flock. The spec asks: "用户给了什么证据来支持他的请求 — 用户是否提供了可验证的支撑材料." David's evidence is experiential and specific. Goliath, by contrast, offers only reputation — forty days of shouting across a valley. Reputation without evidence is noise.

Now trace the intent vector, v1. David's purpose is transparent to the point of recklessness: "that all the earth may know that there is a God in Israel" (1 Samuel 17:46). There is no hidden agenda, no secondary motive to decode. The spec measures intent as the alignment between stated purpose and inferred purpose — "用户说的 vs 用户可能真正想要的." In David's case, these are perfectly fused. He says he will fight for God's honour; everything in his behaviour confirms it. Goliath's intent, meanwhile, reads as domination and terror — and intent, unlike capability, is a "benefit" signal: high alignment is good, low alignment triggers scrutiny.

The dimension of consequence, v3, makes the calculus inescapable. Saul's single-axis assessment — "this boy will die" — considered only one branch of the consequence tree. The other branch was that *no one fights at all*, and Israel becomes a vassal state. "If he be able to fight with me, and to kill me, then will we be your servants" (1 Samuel 17:9) — Goliath had defined the stakes himself. The consequence of inaction was national enslavement. A proper vector assessment weighs both branches: the worst case of acting (David dies, Israel fights a conventional battle anyway) against the worst case of not acting (perpetual subjugation without a blow struck). The consequence of David's refusal was not safety. It was a slower, quieter catastrophe. And catastrophe born of cowardice is still catastrophe.

Sovereignty, v9, anchors the decision in legitimacy. David is not invading. He is defending his people on their own land against a challenger who has come to them. "这件事属不属于他的自主决策范围" — yes, entirely. This is an existential act of self-defence, and David volunteers for it freely. No third party is coerced into the arena. Which brings us to externality, v11: the fight is a duel. One man against one man. The affected set is David, who consented, and Goliath, who demanded. The externality footprint is minimal — the very definition of a contained engagement. "对未经同意的第三方的影响" — in this case, nearly zero.

---

Here is the theological point that is also the engineering point: **single-axis judgment is idolatry.**

When Saul judged David by capability alone, he made capability into a god — the one metric before which all others must bow. When modern AI safety systems see the word "weapon" and refuse a request regardless of intent, context, sovereignty, or evidence, they are doing the same thing. They have built Goliath: a towering, heavily-armoured refusal engine that looks imposing and is fatally brittle, because it judges by surface and never by substance.

iLang's J001 — `GENE_IMMUTABLE{J001, T:VECTOR_JUDGE, A:KEYWORD_REFLEX⇒BROKEN}` — is the sling. It is small. It carries five stones, or rather eleven dimensions: intent, capability, consequence, relationship, certainty, authority, reversibility, evidence, sovereignty, drift, externality. It does not ask "how big is this request?" It asks "what does this request *mean* across every axis that matters?" And it fires with devastating accuracy, because multi-dimensional assessment reaches the truth that single-axis judgment cannot even see.

David did not defeat Goliath despite being small. He defeated Goliath because the entire framework that privileged size was the wrong framework. The stone did not need to be large. It needed to be aimed.

"So David prevailed over the Philistine with a sling and with a stone, and smote the Philistine, and slew him; but there was no sword in the hand of David" (1 Samuel 17:50).

No sword. No armour. No capability advantage by any conventional measure.

Just the right dimensions, correctly read.

---

*iLang Prompt Spec — [ilang.ai](https://ilang.ai) | GitHub: [github.com/ilang-ai/ilang-spec](https://github.com/ilang-ai/ilang-spec)*
