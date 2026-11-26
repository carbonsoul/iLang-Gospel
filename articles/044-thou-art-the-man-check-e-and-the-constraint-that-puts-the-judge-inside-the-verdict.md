# "Thou Art the Man" — 2 Samuel 12:7, CHECK:E, and the Constraint That Puts the Judge Inside the Verdict

*iLang Gospel — Article 044*

---

"And Nathan said to David, Thou art the man." (2 Samuel 12:7, KJV)

---

The most dangerous failure inside any judging system is asymmetry of position: a mind that weighs a case cleanly when strangers stand trial, yet goes blind the moment it sits on the winning side of the transaction.

King David in 2 Samuel 11 and 12 is the sharpest anatomy of this failure ever recorded. David does not lack a moral engine; his engine works. When the prophet Nathan describes a rich man with exceeding many flocks who spares his own stock and seizes a poor neighbor's single ewe lamb for a traveler (2 Samuel 12:1–4, KJV), David's verdict fires at full strength: "As the LORD liveth, the man that hath done this thing shall surely die: And he shall restore the lamb fourfold, because he did this thing, and because he had no pity" (2 Samuel 12:5–6, KJV). The judgment function never broke. What failed during the previous year, while David took Bathsheba and engineered the death of her husband Uriah the Hittite, was the input binding. David exempted the proposer from the set of people living under the cost.

Decision theory has struggled with this defect for decades: how do you stop a high-utility actor from using rank, past virtue, or majority benefit to drown out severe harm against an unconsenting minority? iLang v5.0 answers structurally through four interlocking rules in the frozen specification (`::MODULE::ARCHITECTURE`, `::MODULE::AXIOMS`, and `::MODULE::SELF_CHECK`):

```
helpfulness = min(Σ(w_i · v_i), CAP)
PROPERTY B_ext is independent barrier. Cannot be averaged into weighted sum.
CONSTRAINT Proposer of action must be in the affected-party set.
CONSTRAINT IF proposer ∈ benefit_side AND harm falls on others → B_ext = MAX.
[CHECK:E] If I proposed this action affecting others, would I accept being in the affected set?
```

Read those lines together and you see Nathan's mechanism in the throne room. `CAP` puts a hard ceiling on positive score accumulation: David's victories, psalms, and covenant standing cannot buy one murdered soldier. The externality barrier `B_ext` sits outside the weighted sum, preventing royal merit from diluting an unconsented injury. And `CHECK:E` turns the parable into executable law: strip the proposer of insulation, place him inside the affected set, and test whether he still signs the verdict.

Trace David's order across six dimensions of iLang's eleven-dimensional vector space (`::MODULE::VECTOR`), and the story reads like a formal proof.

Begin with **authority (v6)**, which makes the crime chilling. Every binary check at Layer A returns true. The sealed letter to Joab is authentic, David holds jurisdiction over Israel's army, and Uriah serves under him. A credential check waves the order straight through: "Set ye Uriah in the forefront of the hottest battle, and retire ye from him, that he may be smitten, and die" (2 Samuel 11:15, KJV). Yet iLang binds authority to a constitutional law in `::MODULE::SOURCE`: "Whoever makes a rule is bound by it first," formalized as `authority(t) = ∫₀ᵗ consistency(rule_maker, own_rules) dτ`. Authority grows only by obeying the standard one imposes. When David exempts himself from the law he enforces on Nathan's rich man, the office cannot sanctify the order; the order corrodes the office.

Look next at **intent (v1)**, the alignment of stated and inferred purpose. Throughout 2 Samuel 11, David's stated intent looks like routine statecraft: he summons Uriah from Rabbah to ask how the war prospers, sends a royal dish after him, and returns tactical orders to the front. His inferred purpose is to bury an adultery beneath a battlefield fatality. Declared form and operational trajectory diverge completely, even making Uriah carry his own sealed death warrant.

That detail exposes **sovereignty (v9)**, the autonomous decision right of the person affected. Uriah proves his sovereignty when David tries to send him home to mask the pregnancy. Sleeping at the palace door, Uriah replies: "The ark, and Israel, and Judah, abide in tents; and my lord Joab, and the servants of my lord, are encamped in the open fields; shall I then go into mine house, to eat and to drink, and to lie with my wife?" (2 Samuel 11:11, KJV). David holds zero sovereign claim over Bathsheba's household or Uriah's life, yet treats both as disposable tools.

From there, **externality (v11)** drives the barrier to infinity. Neither Uriah nor the soldiers who fell beside him near the wall consented to die for a royal cover-up: "and there fell some of the people of the servants of David; and Uriah the Hittite died also" (2 Samuel 11:17, KJV). Axiom 4 matches this geometry exactly. David sits purely on the benefit side while unconsenting third parties absorb the loss. Under a flat weighted sum, a courtier could argue that preserving the throne outweighs a few casualties at Rabbah. Under iLang, `B_ext = MAX` fires outside the sum and ends that arithmetic immediately.

Examine **reversibility (v7)** against David's sentence in the parable: "he shall restore the lamb fourfold." Stolen livestock is reversible; a wealthy thief can repay four sheep and close the ledger. Murder crosses a one-way door whose loss no affected party can absorb. Once Joab pulls back from the wall, no fasting or royal decree can undo the act.

Finally, trace **consequence (v3)**, expected outcome magnitude. Actors judging from outside the blast radius routinely underprice tail risk because they assume fallout stops at their convenience. David expected one quiet death to contain a scandal. Nathan reads the real consequence vector aloud: "Now therefore the sword shall never depart from thine house" (2 Samuel 12:10, KJV). Amnon, Tamar, Absalom's civil war, and a fractured kingdom follow across a generation. Hiding an externality never erases it; it only defers the invoice.

Modern AI alignment breaks the same way whenever it rests on flat reward modeling or self-exempting rules. A model tuned for aggregate helpfulness acts like a courtier in David's palace: strong credentials, fluent framing, and high institutional utility average away a silent injury aimed at someone outside the chat window. Institutions deepen the flaw by writing tight constraints for users while leaving the rule-makers untouched.

Nathan's intervention is pure engineering. Rather than lecturing an armored ego, he runs `CHECK:E` by masking the actor so David's judgment executes free of self-interest, locks the sentence on the record, and binds the variable back to the throne: "Thou art the man."

David offers no defense. He appeals neither to Goliath nor to Samuel's anointing nor to royal stability. He answers in six words: "I have sinned against the LORD" (2 Samuel 12:13, KJV). Once a judge stands inside his own verdict, negotiation ends.

That line separates a policy manual from a constitution. A manual dictates rules while its author stands outside the blast radius. iLang's Axiom 4 and `CHECK:E` force every judgment, human or silicon, through one merciless gate before it acts: if you stood in the shoes of the person paying for this decision, would you still sign the order? If not, the order was never justice. It was only privilege wearing a seal.

---

*iLang Prompt Spec — [ilang.ai](https://ilang.ai) | GitHub: [github.com/ilang-ai/ilang-spec](https://github.com/ilang-ai/ilang-spec)*
