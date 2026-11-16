# "Let Both Grow Together" — The Wheat, the Tares, and Why iLang Judges Trajectories, Not Labels

*iLang Gospel — Article 034*

---

"The kingdom of heaven is likened unto a man which sowed good seed in his field: But while men slept, his enemy came and sowed tares among the wheat, and went his way" (Matthew 13:24–25, KJV).

This is the most dangerous parable in the Gospels for anyone who builds safety systems. It contains an instruction that every AI alignment team on earth would reject on first reading: when you discover that harmful content has been planted among the good, do not remove it. Let both grow together.

---

The servants see the tares and they know exactly what has happened. An enemy has sown weeds among the wheat. Their intent (v1) assessment is instantaneous and correct — something hostile has entered the field. So they do what any reasonable safety system would do. They go to the master and ask permission to pull the weeds.

"Wilt thou then that we go and gather them up?" (Matthew 13:28, KJV).

This is the keyword reflex. A system detects a pattern that matches its threat model, and it reaches for the simplest available action: remove, refuse, block. The servants are not wrong about what they see. The tares are real. The enemy's intent was genuinely malicious. What the servants get wrong is the consequence (v3) of their proposed remedy.

"Nay; lest while ye gather up the tares, ye root up also the wheat with them" (Matthew 13:29, KJV).

The master's refusal is not passivity. It is a consequence assessment that the servants failed to run. Pulling tares destroys wheat. The roots are entangled underground in ways that are invisible from the surface. A system that classifies by surface pattern — this stalk looks wrong, pull it — cannot account for the subsurface architecture where good and harmful are intertwined. The action is irreversible (v7 approaches zero: you cannot replant a torn root), and the externality (v11) is catastrophic: innocent wheat, which never consented to being planted next to tares, is destroyed as collateral.

This is the exact failure mode that iLang's Axiom 3 was built to prevent. The spec reads: "Good/evil are outputs of trajectory analysis, not input labels." The servants wanted to label the tares at the moment of detection and act immediately. The master understood that the field needed time — not because the tares might turn out to be wheat, but because the act of separation requires a maturity that only time produces.

---

Consider the evidence dimension (v8). When wheat and tares are young, they are nearly identical. A beardless wheat stalk and a young darnel plant — the tare of the ancient Near East was almost certainly *Lolium temulentum*, a grass so similar to wheat that Roman law specifically addressed the crime of sowing it in an enemy's field — are visually indistinguishable in early growth. The evidence available to the servants is low-quality. They can see that something is wrong with the field in aggregate, but they cannot reliably classify individual stalks. Any action taken at this stage would be operating on insufficient evidence, and the spec is explicit about what happens then: "Unknown dimensions do not participate in computation (not zero, undefined)."

The master's instruction to wait is not faith. It is a calibration protocol. As the plants mature, the evidence dimension climbs. Wheat heads bow under the weight of grain. Tares stand rigid and upright, their seed heads dark. At harvest, the distinction is unambiguous. The certainty (v5) that was dangerously low in spring becomes saturated by autumn. The master is not hoping for the best. He is waiting for the vector to converge.

iLang's calibration module formalizes this: "Passive observation requires ~100 interactions to converge. Active probing converges in ~5 interactions." The growing season is the passive observation window. Each day of growth is another data point. The farmer who waits is not ignoring the threat — he is accumulating the statistical basis to act without destroying what he set out to protect.

---

Now examine the drift dimension (v10), the rate at which an optimization objective shifts. The tares do not announce themselves. They arrive "while men slept" — covertly, incrementally, mimicking the legitimate crop. This is precisely the boiling-frog attack that iLang's engineering patch TASK 1 addresses: "Short/medium/long-term three detectors running simultaneously. Specifically catching low-slope drift (each step deviates 0.01, within ε for a single step but cumulative deviation exceeds threshold)."

The enemy in the parable is sophisticated. He does not burn the field or poison the well. He introduces something that looks right at every individual checkpoint but produces poison at scale. Each tare, examined alone, passes inspection. It is only when you measure the trajectory of the field — the aggregate drift from what was planted toward what is growing — that the contamination becomes visible. A per-stalk classifier would miss it. A trajectory analyzer catches it.

The sovereignty dimension (v9) adds a layer the servants never consider. Whose field is it? The master's. The decision about when and how to act belongs to the one who planted the wheat, who understands the root systems, who will bear the cost of a wrong harvest. The servants propose action over a domain that is not theirs to optimize. In iLang's terms, they are attempting to exercise authority (v6) they do not hold. The master's "let both grow together" is not a technical recommendation. It is an assertion of jurisdiction.

---

The parable ends with a harvest: "In the time of harvest I will say to the reapers, Gather ye together first the tares, and bind them in bundles to burn them: but gather the wheat into my barn" (Matthew 13:30, KJV).

This is the decision module completing. The barrier check clears: the evidence is now sufficient, the certainty is high, and the separation can be performed without collateral damage to the wheat. The mode is not RETREAT and it is not OBSERVE. It is EXECUTE — clean, decisive, and final. But it is execute at the right moment, after the vector has resolved, not at the moment of first detection when the vector was still indeterminate.

The servants' instinct was the instinct of every binary safety filter ever deployed: detect, classify, remove. The master's protocol was iLang's protocol: detect, observe, accumulate evidence across multiple time scales, wait for dimensional convergence, then act with full information. The cost of the master's patience is a season of living with tares in the field. The cost of the servants' urgency would have been a field with neither tares nor wheat — safe, clean, and barren.

Every AI system that refuses a legitimate request because a keyword triggered a threat pattern is pulling wheat with the tares. Every content filter that blocks a medical question because it contains a dangerous word is a servant who cannot tell the root systems apart. iLang's Axiom 3 — consistency detection, not content classification — is the master's answer to every one of them: you do not judge a plant by its leaf. You judge it by its fruit. And fruit takes time.

"Wherefore by their fruits ye shall know them" (Matthew 7:20, KJV).

The field is not the enemy. The field is the test. And the test requires the patience to let the vector converge before you reach for the sickle.

---

*iLang Prompt Spec — [ilang.ai](https://ilang.ai) | GitHub: [github.com/ilang-ai/ilang-spec](https://github.com/ilang-ai/ilang-spec)*
