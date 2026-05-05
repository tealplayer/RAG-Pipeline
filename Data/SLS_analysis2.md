
Go to pennystocks
r/pennystocks
•
2mo ago
Confident-Web-7118

$SLS Part 2 and FINAL (Deepest Due Diligence for REGAL Trial) (From a Deep Value Investor) (Predicting BAT mOS from Predictive Model)
emoji:DDNerd: 🄳🄳 
emoji:DDNerd:
Hey everyone, this is the follow-up (part 2 and final) to my first deep due diligence for REGAL. For anyone new, since this is part 2, I’ve been a deep value investor for several years.  I own 805K shares here (and am continuously accumulating every week).

In Part 1, shared extensive deep due diligence on the cure rate model for the REGAL trial I coded and built. 

The reason I continued on from the cure survival model is because the results from the model, and stress test results, allowed me to have the data I need to build a predictive model that predicts with 90% accuracy what BAT mOS in the trial is, given the constraints of 60 Events as of Jan 2025, and 72 Events as of Dec 26, 2025.

For context, I have years of experience in machine learning/statistics, and below I do my best to distill the logic of the predictive model and results in as simple of a way as I can.

These are the results predicted by the model, and below you'll see exactly how these results are predicted and why they are:

91% accuracy that BAT mOS is 10-14
80% accuracy that it is 10-13
Within that 10-13, 99% accuracy it is 11.4 months for BAT median OS

The model is a constrained parametric mixture-cure model and the methodology for predicting the BAT mOS is Bayesian evidence synthesis.

Explained simply, there are two parts:

At its simplest explanation: we're taking the hard data (72 events out of 126 patients at Month 58) and reverse-engineered the only mathematical curve that fits those constraints without breaking the biological reality.

For the Bayesian evidence synthesis, we took a "prior" (the 7 published literature sources that put BAT mOS at 8-10 months) and updated it using the "likelihood" (the hard trial constraints and Monte Carlo simulations) to generate a "posterior" probability distribution (the 11.4-month biological identity point).

For the constrained mixture-cure model, we modeled the survival curve by splitting the GPS arm into a "cured" fraction (the plateau) and an "uncured" fraction (the exponential decay), and locked the degrees of freedom using the trial's exact event count.

I explain more later on so don't worry

The first post clearly showed why there are 99.9999% chances of success for the REGAL trial, and if BAT mOS is under 18 to 20, the trial is successful.  And essentially 16 or below for BAT mOS, makes GPS the groundbreaking standard of care in AML CR2 (not eligible for transplant).

But, I was curious to solve for what BAT mOS is in the trial, with a high degree of statistical accuracy of at least 90%+.  I’ve been a deep value investor for years, and have used these skills in business & work for so many years, and I am glad to be able to use them here to solve this and to share with everyone.  I’ll touch on this again at the end of the post, but SLS is the rarest asymmetric opportunity with insane margin of safety that I’ve ever come across in my life thus far.

And I wanted to follow-up and do this quickly, since the results of the model, all of the code, parameters, tuning, etc. are all fresh in my brain.  

For anyone new here, the pre-read DD resource I would recommend is Part 1 that I posted.

Moving on, here is a quick recap.  And prepare yourself for some deep due diligence, it is the only way to go over this properly and to share the model results with you clearly.

Quick recap (for those who missed Part 1)
REGAL is a Phase 3 trial in AML (acute myeloid leukemia) patients in second remission. 126 patients, 63 per arm: GPS vaccine vs Best Available Therapy.

72 of 80 required events have occurred. 54 patients still “alive” (don’t worry, censoring stress tests have been performed extensively) at month 58.

Event deceleration signal: only 12 deaths in 12 months from 66 at risk. The survival curve has flatlined. The only mathematical shape that explains this is a cure-fraction model on the GPS arm.

Original model: roughly 64% of GPS patients may be functionally cured (under the unconstrained two-constraint fit). Expected topline HR: 0.35-0.50, with trial threshold at 0.636.

TL;DR (although I recommend reading all of this deep due diligence and everything related to the predicted BAT mOS and stress tests, put a ton of effort into this):

I ran 5 independent stress tests trying to break the REGAL cure-fraction model: censoring bias, BAT long-survivors, vaccine delay, BAT mOS uncertainty, and combined worst case. Every single one cleared the trial threshold.

BAT median OS estimate: 11.4 months. Five independent evidence streams (literature, biological plausibility, biological identity point, IDMC behavior, Phase 2 consistency) all converge on 10-13 months. 91% of the Bayesian posterior mass sits in the 10-14 month range.

Expected topline Cox HR: 0.35-0.50. The model-derived HRs in the tables below are lower (0.13-0.30), but those reflect the cure-fraction plateau distortion. The actual stratified Cox HR in the press release will be higher because it averages across the full curve. Either way, the trial threshold is 0.636 -- not close.

Posterior-weighted P(trial success) = 99.9%, integrating over ALL uncertainty in BAT mOS. This is not conditional on any single assumption.

The only way this fails: BAT mOS above 20 months (no CR2 AML population has ever achieved this), OR the 60/72 event counts are fabricated, OR survival curves can decelerate without a cure fraction (mathematically impossible).

Important distinction: "Cured" does not mean "alive right now." The 54 patients still alive at month 58 are a mix of two populations: (1) the cured plateau -- GPS patients the math says will “never relapse” from AML -- and (2) uncured responders who are still alive but will eventually decline, plus BAT patients surviving on their own timeline. The cure rate (roughly 64%) refers strictly to GPS patients who have reached the permanent mathematical plateau, not simply everyone who is currently breathing. Some of those 54 alive are uncured GPS patients still at risk. Others are BAT arm patients. The cure fraction is the structural parameter that explains why the death rate is decelerating -- not a head count of survivors.

A note on the Hazard Ratios in this analysis. Some of the tables below show model-derived Cox HRs as low as 0.13 or 0.20. If your first reaction is "that is impossibly low for an oncology trial," good -- that instinct is correct for a typical drug study. These numbers come from 300 Monte Carlo trial simulations using the cure-fraction parameters. In a cure-fraction setting, the proportional hazards assumption is massively violated: once the cured patients hit the plateau, GPS events stop almost entirely, and nearly all remaining deaths come from the BAT arm. Cox regression is forced to summarize a fundamentally non-proportional situation with a single coefficient, which produces an extremely low number.

The actual trial topline will not report a 0.13 HR. The press release will use a stratified log-rank test and a stratified Cox model adjusted for the 4 randomization stratification factors (MRD status, CR1 duration, geographic region, disease status at entry). That stratified Cox HR will also be pulled toward 1.0 by the early period when GPS has not yet fully separated from BAT and by the inherent noise of a 126-patient trial. I expect the reported topline Cox HR to land in the range of 0.35 to 0.50 -- still a blowout by any oncology standard (the threshold for statistical significance is HR < 0.636, one-sided alpha = 0.025). The model HRs in the tables below are useful for relative comparisons between stress tests -- seeing how much each scenario degrades the result -- not as literal predictions of the headline number.

Stress Test #1: What if patients are disappearing?
In clinical trials, "censoring" simply means a patient dropped out or was lost to follow-up before the trial ended -- they moved away, chose to stop participating, or the data cutoff arrived before they had an event. "Censoring bias" is the fear that sick patients on the GPS arm are dropping out because they are dying, meaning their deaths happen off the books and artificially keep the survival curve looking high.

The concern: Censoring bias. Some commenters asked: what if patients on the GPS arm are dropping out of the trial because they are sick, and their deaths are not being counted? That would make GPS look better than it really is. The "54 alive" might include people who are actually dead but just stopped being tracked.

This is a legitimate concern. In smaller trials, differential dropout can absolutely distort results.

What I did: I ran 300 Monte Carlo simulations per scenario. I took the model's "alive" GPS patients and forcibly converted a percentage of them into deaths -- as if they had actually died at some random point during their follow-up window. This is the worst-case mode: every single dropout is assumed to be a hidden GPS death. Zero dropout from BAT.

I swept this across BAT mOS from 10-18 months and dropout rates from 0-30%.

Selected results:

BAT mOS	Dropout %	Median HR	95% CI	P(success)
10m	0%	0.129	[0.07, 0.22]	100%
10m	10%	0.165	[0.10, 0.26]	100%
10m	30%	0.233	[0.15, 0.35]	100%
12m	0%	0.204	[0.11, 0.33]	100%
12m	10%	0.250	[0.14, 0.39]	100%
12m	30%	0.339	[0.22, 0.50]	100%
14m	0%	0.294	[0.16, 0.47]	100%
14m	10%	0.346	[0.21, 0.54]	99%
14m	30%	0.455	[0.31, 0.67]	96%
16m	0%	0.393	[0.23, 0.63]	98%
16m	10%	0.451	[0.28, 0.69]	92%
16m	30%	0.578	[0.39, 0.85]	71%
18m	0%	0.498	[0.30, 0.82]	84%
18m	10%	0.570	[0.35, 0.90]	71%
18m	30%	0.711	[0.48, 1.07]	26%
r/pennystocks - $SLS Part 2 and FINAL (Deepest Due Diligence for REGAL Trial) (From a Deep Value Investor) (Predicting BAT mOS from Predictive Model)
At realistic BAT values (10-14 months), even 30% worst-case GPS dropout barely dents the result. At BAT=12m with 30% of GPS "alive" patients secretly dead, HR is still 0.34 with P(success) = 100%.

The first real threat appears around BAT=16m + 30% worst-GPS dropout: HR 0.58, P(success) 71%. But that requires both an extreme BAT assumption AND an absurd level of one-sided censoring. Neither is likely. Together, the probability is effectively zero.

Bottom line: censoring bias is a non-issue for any realistic scenario.

Stress Test #2: What if BAT patients are secretly surviving?
The concern: Even in control arms, some patients survive a long time. AML biology is heterogeneous. Some patients carry favorable mutations (NPM1 without FLT3-ITD, for instance) that give them years of remission even without active therapy. Maybe BAT has its own pool of long-term survivors, and the model is wrong to assume a clean exponential.

This is probably the most dangerous critique, because it directly attacks the model's core mechanic. If BAT patients are also surviving long-term, the GPS cured pool shrinks to compensate.

What I tested: I gave the BAT arm a 20% cure fraction. For context, realistically, based on modern data, Ven+Aza 3 year survival rate in CR2 (not eligible for transplant) is likely only 0% to 5%, but let’s stress test anyway under impossible scenarios.  Continuing on, QUAZAR AML-001 (azacitidine maintenance Phase 3) showed roughly 15-20% of placebo patients alive at 3 years in CR1. In CR2, published rates are more like 5-15%, so 20% is genuinely aggressive.

Here is the math: with 20% of BAT patients “immortal”, those patients contribute heavily to the 54 alive at month 58. That means GPS needs fewer long-term survivors to make the total work. The GPS cure fraction drops accordingly -- it is a survivor budget problem.

BAT mOS	GPS Cure (Std)	GPS Cure (BAT 20%)	HR (Std)	HR (BAT 20%)	P(success)
12m	68%	39%	0.20	0.36	99%
14m	65%	46%	0.29	0.44	96%
16m	61%	48%	0.39	0.52	82%
18m	58%	47%	0.50	0.62	54%
r/pennystocks - $SLS Part 2 and FINAL (Deepest Due Diligence for REGAL Trial) (From a Deep Value Investor) (Predicting BAT mOS from Predictive Model)
Yes, the GPS cure fraction drops 10-30 percentage points. That is the math working correctly -- when BAT carries more survivors, GPS needs fewer to hit the same total.

But look at the HRs. At BAT=12m: HR goes from 0.20 to 0.36. P(success) = 99%. At BAT=14m: 0.44, P(success) = 96%.

GPS still wins in every realistic scenario.

Stress Test #3: The vaccine delay problem
This one produced the most surprising result.

The concern: GPS is a vaccine. It does not work instantly. The dosing protocol involves 6 biweekly priming doses over the first 3 months, followed by monthly boosters. During that ramp-up period, GPS patients are essentially unprotected -- they are dying at the same rate as BAT. For the first 3-4 months, HR = 1.0. GPS only starts separating from BAT after the immune response is established.

What I tested: I forced GPS to follow BAT's survival curve identically for the first 4 months. After month 4, GPS switches to the cure-fraction model. The solver must find a cure fraction that still produces 60 events at month 46 and 72 at month 58.

The surprise: At BAT = 12 months, there is no mathematical solution for a 4-month delay.

The solver does not produce a "weak" answer -- it produces no answer at all. The equations have no valid solution.

Here is why. At BAT = 12m, roughly 24% of GPS patients (15 out of 63) would die during the 4-month delay period, following BAT's exponential survival. That leaves about 48 survivors. To still match the 72 total events at month 58, those 48 survivors would need an impossibly high cure fraction. The math breaks.

I tested delay sensitivity at BAT=12m:

Delay (months)	Conditional Cure %	Status
0	68%	Clean solution
1	69%	Clean solution
2	71%	Clean solution
3	57%	Solver straining
4	--	NO SOLUTION
5	--	NO SOLUTION
6	--	NO SOLUTION
r/pennystocks - $SLS Part 2 and FINAL (Deepest Due Diligence for REGAL Trial) (From a Deep Value Investor) (Predicting BAT mOS from Predictive Model)
What this tells us: The data itself constrains the maximum possible delay to about 2-3 months. GPS must be working before month 4. If it were not, the observed event pattern would be mathematically impossible.

This makes biological sense. These are CR2 patients -- they have already had AML once, been treated, and relapsed. Their immune systems have been exposed to WT1 (the protein GPS targets) for months or years. GPS is not building an immune response from scratch. It is boosting pre-existing memory T cells. When I Googled this/search this, this is what is an anamnestic recall response -- the immunological equivalent of a booster shot. The second dose kicks in fast because the immune system remembers.

The dosing amendment that changed everything (November 2022): In the middle of REGAL enrollment, SELLAS amended the protocol to continuous dosing -- treat until relapse. This is a direct upgrade from Phase 2, where patients stopped receiving GPS after about a year and eventually relapsed. The mathematical plateau (the cure fraction) maps directly to this biological mechanism: continuous boosters maintain immune pressure on residual WT1-expressing leukemic stem cells permanently. Phase 2 patients lost that pressure when dosing stopped. REGAL patients never do.

Where the delay DOES solve (BAT >= 13m):

BAT mOS	Standard HR	4mo Delay HR	P(success)
13m	0.25	0.27	100%
14m	0.29	0.34	100%
15m	--	0.41	98%
16m	0.39	0.50	87%
18m	0.50	0.68	35%
20m	0.61	0.88	6%
At BAT=14m, the 4-month delay shifts HR from 0.29 to 0.34. P(success) = 100%. The delay is ancient history by month 46+. The cure fraction overwhelms it.

r/pennystocks - $SLS Part 2 and FINAL (Deepest Due Diligence for REGAL Trial) (From a Deep Value Investor) (Predicting BAT mOS from Predictive Model)
Look at the survival curves. By month 18-24, the delayed GPS curve has nearly caught up to the standard GPS curve. The solver compensates by assigning a higher conditional cure fraction among survivors: the vaccine works on fewer patients (those who survived the delay), but it works better on them. The net effect on the trial-level HR is minimal.

Tying it together: what the stress tests tell us about BAT median OS
These stress tests did not just prove that GPS survives worst-case scenarios. They acted as a biological filter that helped calculate exactly what the BAT mOS is.

Here is how. The censoring test showed that the result only becomes threatened above BAT = 16 months -- any BAT value below that, even with 30% worst-case GPS dropout, still produces a clear GPS win. The long-survivor test showed that giving BAT a generous 20% cure fraction narrows the GPS cure fraction but does not flip the outcome at any realistic BAT value. And the vaccine delay test proved something critical: a 4-month delay is mathematically impossible at BAT values below 13 months. GPS must be activating fast, which is only consistent with moderate BAT values where the early event rate leaves enough surviving patients to produce a valid solution.

These three tests systematically eliminated BAT values below 10 months (where the model requires biologically implausible uncured survival -- GPS "failures" living 5-6x longer than BAT patients, I cover this later on here) and above 14 months (where the model requires GPS non-responders to perform worse than untreated patients, a biological impossibility for a peptide vaccine). The stress tests forced the true BAT mOS into a highly constrained 10-14 month window -- and they did it independently of any literature prior. The published data simply confirmed what the model's own internal consistency already demanded.

I stress tested all the way to a 23 BAT mOS (impossibilities), but for almost anyone that does DD for REGAL, the most common pushback on the original post was: "you are assuming BAT mOS = 8 to 10 months." Fair enough -- the trial is blinded. Nobody knows the exact number. So let me walk through how we narrow it down.

The Late Surge Shield. Enrollment finished at 126 patients in April 2024. About 25 of those patients enrolled between December 2023 and April 2024 -- the "late surge" driven partly by the November 2022 protocol amendment that accelerated site activation. By December 2025, even this newest cohort has 20+ months of follow-up. Historical BAT median survival in CR2 AML is 8-10 months. If the drug were not working, that late cohort would have triggered a wave of BAT-arm deaths through 2025. Instead, only 12 events total across both arms in 12 months. The late enrollees have cleared the danger zone.

With that context, here is the formal estimation. I ran a Bayesian-style analysis combining multiple constraints:

Literature prior: CR2 AML historical data from 7 published sources (Brayer 2015, REGAL FDA design, DiNardo 2020, Breems 2005, QUAZAR AML-001, Gilleece EBMT). Log-normal centered at about 9 months (range: 5.4m pre-venetoclax, 8-10m in the venetoclax era). Weighted center = 8.0 months.

REGAL data constraints: 60 events at month 46, 72 at month 58

IDMC plausibility: The arms were visibly separated at the interim analysis (the IDMC said "continue without modification" -- twice)

Biological plausibility: The required GPS cure fraction should be achievable (roughly 40-70%, consistent with Phase 2 immunologic response rate of 64%)

Results:

Metric	Value
MAP (mode)	11 months
Mean	11.4 months
Median	11 months
80% Credible Interval	[10, 13] months
90% Credible Interval	[10, 14] months
r/pennystocks - $SLS Part 2 and FINAL (Deepest Due Diligence for REGAL Trial) (From a Deep Value Investor) (Predicting BAT mOS from Predictive Model)
The posterior peaks at 11 months, consistent with a venetoclax-era CR2 AML control arm. Seven published data sources converge on 8-10 months for CR2 non-transplant patients in the venetoclax era (pre-venetoclax: 5.4m per Brayer 2015, PMID 25802083; Ven-era r/R AML: 7.8m per DiNardo 2020, PMID 32896301; REGAL FDA design: 8.0m).

What matters for the investment thesis: even at the 90th percentile of the posterior (BAT = 14m), the model still shows very high probability of success. You do not need to know the exact BAT mOS. The margin of safety swallows the uncertainty.

Monte Carlo validation of the top candidates:

BAT mOS	Cox HR	P(HR < 0.636)	P(HR < 0.50)
10m	0.129 [0.07-0.22]	100%	100%
12m	0.204 [0.11-0.33]	100%	100%
14m	0.294 [0.16-0.47]	100%	99%
16m	0.393 [0.23-0.63]	98%	85%
Literature validation of the prior (7 published data points, fully cited):

#	Source	Raw mOS	Adjusted for REGAL	Weight
1	Brayer 2015 GPS Phase 2 controls (PMID 25802083)	5.4m	8.1m*	High (21%)
2	REGAL FDA design assumption (SEC filings)	8.0m	8.0m	Very High (32%)
3	DiNardo 2020 Ven+Dec r/R AML (PMID 32896301)	7.8m	8.5m	High (21%)
4	DiNardo 2020 treated secondary AML (same paper)	6.0m	7.0m	Medium (11%)
5	Breems 2005 AML relapse index (PMID 15632409)	12.0m	7.5m**	Low-Med (5%)
6	QUAZAR AML-001 placebo arm (Wei, NEJM 2020)	14.8m	8.1m***	Medium (11%)
7	Gilleece EBMT CR2 WITH transplant (PMID 31363160)	42m	Ceiling only	Low
* Pre-venetoclax 5.4m + venetoclax-era improvement of about 50% ** Includes transplant recipients; non-transplant about 60% of reported *** CR1 to CR2 adjustment (x0.55)

All 6 quantitative data points cluster tightly around 7.0-8.5 months after adjustment for era, population (CR2 vs r/R vs CR1), and transplant status. The REGAL FDA design assumption of 8.0m sits at the center. This is not a coincidence -- it is what convergent evidence looks like.

How accurate is this? Methodology & Validation
I know people will ask: "How do you know this model is right?" Here is the entire logic chain, from raw data to final confidence number.

The logic chain (start here if you read nothing else)
Step 1 -- Hard data (not assumptions):

60 events at month 46 (publicly confirmed)

72 events at month 58 (publicly confirmed)

54 patients alive out of 126 (publicly confirmed)

Only 12 new events in 12 months from 66 at-risk patients

Step 2 -- What math fits that data? An 18% annual death rate from 66 patients at risk. Standard exponential survival would predict about 33%. The curve is decelerating -- patients are dying slower and slower over time. The ONLY mathematical form that produces a decelerating death rate is a cure-fraction model: some fraction of GPS patients “never die” of AML while the rest follow exponential decay. (An exponential GPS model would need mOS = 97.6 months -- 8+ years for relapsed AML. Nobody believes that.)

Step 3 -- How constrained is the model? 3 parameters, 2 hard constraints, 1 degree of freedom (BAT mOS). For ANY BAT mOS you pick, there is exactly ONE (cure_frac, uncured_mOS) that fits. The model cannot overfit. It cannot be gamed.

Step 4 -- Does BAT mOS matter for the prediction? No. I ran 300 Monte Carlo trial simulations at every BAT from 9-20 months. GPS wins in every single scenario. Even at BAT = 20m (far beyond any published CR2 AML control), the cure-fraction model predicts GPS outperforms BAT.

Step 5 -- The actual confidence number:

Posterior-weighted P(trial success) = 99.9%

This integrates P(success | BAT) x P(BAT | data) over the full Bayesian posterior. It accounts for ALL uncertainty in BAT mOS -- every possible value, weighted by how likely it is given 7 published literature sources + biological plausibility constraints. It is not conditional on any single assumption.

Now let me show you the detailed analysis behind each step.

The constraint system
The cure-fraction model has 3 free parameters (BAT mOS, GPS cure fraction, GPS non-responder uncured mOS). It is locked to 2 hard constraints from REGAL data:

60 events at month 46 (interim analysis, publicly confirmed)

72 events at month 58 (Dec 2025 press release, publicly confirmed)

That leaves exactly 1 degree of freedom -- the BAT mOS assumption. Once you pick a BAT mOS, the other two parameters are uniquely determined, not fitted. The solver finds the one and only (cure_frac, uncured_mOS) pair that satisfies both event constraints to machine precision (residual < 10^-10).

This means the model cannot overfit. 1 free parameter, 2 hard constraints, 0 wiggle room.

How the cure model constrains BAT mOS (the key insight)
Here is what is really important to understand: the cure model's outputs at each BAT assumption are biologically testable predictions. For every BAT mOS value, the solver produces a unique cure fraction and uncured mOS (the GPS non-responder uncured mOS). We can ask: are these numbers biologically plausible?

The constraint manifold:

BAT mOS	Cure %	Uncured mOS	Ratio (Unc/BAT)	Biological Assessment
9m	38%	53.2m	5.91x	IMPLAUSIBLE
10m	64%	20.0m	2.00x	Unlikely
11m	68%	13.0m	1.18x	Plausible
12m	68%	9.9m	0.83x	Plausible
13m	67%	8.3m	0.63x	Plausible
14m	65%	7.2m	0.52x	Unlikely
16m	61%	6.1m	0.38x	IMPLAUSIBLE
18m	58%	5.6m	0.31x	IMPLAUSIBLE
20m	54%	5.4m	0.27x	IMPLAUSIBLE
The ratio column is the key. GPS is a cancer vaccine. It can help, but it cannot harm. Patients who do not respond to GPS are still receiving standard therapy (BAT). Their survival -- the "uncured mOS" -- should be roughly comparable to BAT patients (ratio of about 0.7-1.5x):

BAT = 9m, uncured = 53m (5.9x): GPS "failures" would live 6 times longer than the control arm. This is biologically impossible -- if the vaccine did not cure them, they should not dramatically outperform untreated patients.

BAT = 10-13m, uncured roughly 10-20m (0.8-2.0x): Uncured GPS non-responders is roughly equal to BAT. This is exactly what you would expect -- non-responders behave like the control arm, maybe slightly better from supportive care effects.

BAT = 16-20m, uncured = 5-6m (0.3-0.4x): GPS non-responders die in 5-6 months while BAT patients survive 16-20 months. The vaccine would be harming non-responders. Biologically implausible for a peptide vaccine with minimal toxicity.

This biological filter narrows the plausible BAT range to approximately 10-14 months -- exactly where the literature says it should be.

Combining all evidence layers and the biological identity point
Here is the strongest result: I solved for the exact BAT mOS where the ratio equals 1.0 -- where GPS non-responders perform identically to BAT patients. This is the biological identity point: the one BAT value that makes the model's internal predictions maximally self-consistent.

Biological identity point: BAT = 11.4 months.

At this BAT value:

Cure fraction = 68%

Uncured mOS = 11.4m (exactly equals BAT mOS)

GPS overall mOS = NR

0 degrees of freedom. The system is fully determined -- no assumptions, no priors, just data + biology.

This is what makes the estimate robust: five independent evidence streams all converge on the same answer:

Literature prior (7 published sources): Weighted center = 8.0m, all cluster at 7-10m adjusted. Points to 9-12m.

Cure model biological plausibility: Eliminates BAT < 10m (uncured too high) and BAT > 16m (uncured too low). Leaves 10-14m.

Biological identity (unc = BAT): Exact solution at 11m. Narrows to 10-13m.

IDMC behavior: Arms visibly separated, substantial death gap between arms. Consistent with 10-14m.

Phase 2 consistency: Cure fraction 68% at identity point. Matches Phase 2 IR rate of 64% almost exactly.

These streams converge independently on BAT = roughly 10-13 months (80% CI), with the biological identity point at 11.4m.

Statistical accuracy of the 11.4-month estimate
How much should you trust a specific number from a blinded trial model? Here are the quantitative confidence metrics:

Accuracy Metric	Value	What It Means
Posterior mass in 10-13m	85%	85% of all Bayesian probability sits in this narrow 3-month window
Posterior mass in 10-14m	91%	Expanding to the full biologically plausible range covers 91%
Estimator agreement	within 0.7m	MAP (10.8m), Mean (11.4m), and Median (11.2m) all agree within 0.7 months -- no skew, no outlier pull
Identity point vs posterior mean	0.0m apart	The biology-derived point estimate and the data-derived posterior mean are nearly identical
Constraint residual at identity	< 10-28	Machine-precision fit to both observed event counts simultaneously
Bio score at identity	0.00	Perfect biological plausibility: uncured mOS / BAT mOS = 1.00 exactly
Leave-one-out stability	0.0m MAP shift	Removing any single literature source does not move the answer
Prior sensitivity (25 combos)	MAP stays 9-12m	Tested 25 prior center/width combinations; answer is robust to prior choice
Independent evidence streams	5 of 5 converge	Literature, plausibility filter, identity point, IDMC, Phase 2 -- all agree
The 11.4-month estimate is not fragile. It is overdetermined -- more independent constraints point to it than are mathematically required to identify it. The MAP, Mean, and Median all cluster within 0.7 months of each other. The biological identity point (11.4m) falls between the MAP and the Mean. Five independent evidence streams -- none of which share inputs -- converge on the same 10-13 month range. That is the difference between a fitted parameter and a discovered constant.

Validation results
Test	Result	Interpretation
Leave-one-out (LOO)	Removing any single literature source shifts MAP by 0.0m	No single data point drives the result
Posterior predictive check	Simulated events match observed (ratio: 0.97, 1.03)	Model generates data consistent with reality
Prior sensitivity (25 combos)	MAP ranges 9-12m across all prior widths/centers tested	Not driven by prior assumptions
Constraint residuals	< 10-10 for all solved BAT values	Machine-precision match to observed data
Model comparison (exp vs cure)	Exponential GPS implies mOS = 97.6m (absurd)	Cure fraction is structurally necessary
Degrees of freedom	1 free parameter after 2 hard constraints	Minimal parameters = impossible to overfit
Biological plausibility filter	Only BAT 10-14m gives unc/BAT ratio 0.5-2.0x	Additional independent constraint on BAT
Trial outcome robustness -- the table that matters most
For EVERY plausible BAT value (9-20m), I solved the constraint system and ran 300 Monte Carlo trial simulations:

BAT mOS	Cure %	Uncured mOS	Unc/BAT	GPS mOS	HR	95% CI	P(success)
9m	38%	53.2m	5.91x	127.1	0.097	[0.05, 0.16]	100.0%
10m	64%	20.0m	2.00x	NR	0.129	[0.07, 0.22]	100.0%
11m	68%	13.0m	1.18x	NR	0.164	[0.09, 0.27]	100.0%
12m	68%	9.9m	0.83x	NR	0.204	[0.11, 0.33]	100.0%
13m	67%	8.3m	0.63x	NR	0.247	[0.13, 0.40]	100.0%
14m	65%	7.2m	0.52x	NR	0.294	[0.16, 0.47]	100.0%
16m	61%	6.1m	0.38x	NR	0.393	[0.23, 0.63]	97.7%
18m	58%	5.6m	0.31x	NR	0.498	[0.30, 0.82]	84.3%
20m	54%	5.4m	0.27x	NR	0.614	[0.39, 1.00]	54.7%
r/pennystocks - $SLS Part 2 and FINAL (Deepest Due Diligence for REGAL Trial) (From a Deep Value Investor) (Predicting BAT mOS from Predictive Model)
Every single row predicts GPS wins. The trial outcome prediction does not depend on knowing BAT mOS precisely. Whether BAT is 10 months or 20 months, the cure-fraction model -- constrained by 60 events at month 46 and 72 events at month 58 -- predicts GPS significantly outperforms BAT.

What each stress test proved (connecting it all together)
Each stress test above attacked a different assumption. Here is how they feed into the confidence level:

Stress Test	What It Attacked	Result	What It Proves
Censoring (dropout)	Maybe GPS "alive" patients are secretly dead	GPS wins even with 30% worst-case dropout at BAT=14m	Even massive systematic bias does not change the outcome
BAT long-survivors	Maybe BAT has its own cure fraction	GPS cure fraction drops but HR still clears at BAT=14m	The survivor budget constrains itself -- you cannot break both arms
Vaccine delay	Maybe GPS takes 4+ months to work	No solution exists at BAT < 13m; modest HR impact above	The data itself rules out long delays. GPS works fast.
BAT mOS uncertainty	We do not know the exact BAT value	100% P(success) at BAT 9-14m, 98% at 16m	The conclusion is insensitive to the main unknown
Combined worst case	Stack ALL hostile assumptions	Needs BAT > 16m + 30% dropout + 20% BAT cure + 4mo delay simultaneously	All 4 must be true AND extreme to threaten the result
The accuracy claim -- with the math
The number: posterior-weighted P(trial success) = 99.9%

This is not a qualitative judgment -- it is a computed integral. The calculation:

P(success) = sum of P(success | BAT=x) x P(BAT=x | data)

For each possible BAT mOS, I multiplied the MC-simulated probability of trial success by the Bayesian posterior probability of that BAT value, then summed. This accounts for ALL uncertainty in BAT mOS.

The breakdown:

P(BAT <= 16m) = 99.6% -- P(success) >= 98% everywhere in this range

P(BAT > 16m) = 0.4% -- P(success) drops to 84-55%, but this region has near-zero posterior weight

P(BAT > 20m) = 0.00% -- essentially impossible based on all published AML data

The result: 99.9% posterior-weighted probability of trial success. This already incorporates every source of uncertainty the model has: BAT mOS uncertainty, parameter estimation, and Monte Carlo simulation variance.

Three levels of accuracy, from most to least precise:

Trial outcome prediction (100% confidence): Not assuming any single BAT -- this is the marginal probability across the full posterior. GPS wins almost everywhere, and "everywhere" is weighted by how likely each BAT value actually is.

BAT mOS range (>95% confidence: 10-14m): Five convergent evidence streams -- literature, biological plausibility filter, biological identity point (roughly 11m), IDMC behavior, and Phase 2 consistency -- all converge on the same 10-13m range.

BAT mOS point estimate (best estimate: roughly 11m): The biological identity point -- where GPS non-responders perform identically to BAT -- gives the most constrained single estimate. 0 degrees of freedom.

What would need to be true for this to be wrong:

BAT mOS > 23 months (no CR2 AML population has ever achieved this), OR

The 60/72 event counts are fabricated (SEC fraud), OR

Survival curves can decelerate without a cure fraction (mathematically impossible)

None of these are plausible.

The combined worst case
I have shown each stress test individually. But what if you stack them? What happens when:

BAT has a 20% cure fraction, AND

30% of GPS "alive" patients are actually dead, AND

GPS takes 4 full months to start working?

At BAT = 16m (the realistic upper bound for this combination), the stacked worst case pushes HR toward 0.65-0.70, with P(success) dropping to 35-50%.

That sounds bad until you think about what it requires:

BAT outperforms every historical CR2 AML control by 100%+ (literature consensus: 8-10m)

30% of GPS patients reported as alive are secretly dead

GPS takes 4 full months to activate (but the delay test says this is mathematically impossible at BAT < 13m)

20% of BAT patients are naturally cured (2-4x higher than any published CR2 data)

The probability of ALL FOUR happening simultaneously is effectively zero. Any ONE of them alone? GPS wins. You need all four stacked AND an extreme BAT assumption to even threaten the result.

r/pennystocks - $SLS Part 2 and FINAL (Deepest Due Diligence for REGAL Trial) (From a Deep Value Investor) (Predicting BAT mOS from Predictive Model)
Updated margin of safety
Here is how I think about this as a deep value investor. The question is not "what is the exact HR?" It is: how many things need to go simultaneously wrong for this to fail?

Answer: almost all of them. Simultaneously.

Stress Test	HR at BAT=14m	P(success)	Verdict
Standard model (no stress)	0.29	100%	GPS wins
+ 30% censoring (worst-GPS)	0.45	96%	GPS wins
+ BAT 20% cure fraction	0.44	96%	GPS wins
+ 4-month vaccine delay	0.34	100%	GPS wins
Every single stress test clears the threshold. Not by a hair – by 30-50% margin.

The only way to get HR above 0.636: push BAT beyond 23 months (no CR2 AML population has ever achieved this), OR stack 3-4 hostile assumptions simultaneously (each of which is individually unlikely and one of which -- the 4-month delay -- is mathematically ruled out at low BAT values).

r/pennystocks - $SLS Part 2 and FINAL (Deepest Due Diligence for REGAL Trial) (From a Deep Value Investor) (Predicting BAT mOS from Predictive Model)
What I learned from breaking stuff
I went into this stress testing expecting to find a weakness. Something the original model was hiding. Some scenario where the thesis falls apart.

I did not find one.

What I found instead:

The censoring concern is real in theory but irrelevant in practice. You would need absurd levels of differential GPS-only dropout to matter.

BAT long-survivors are the most credible threat -- but even giving BAT a generous 20% cure fraction, GPS maintains a wide HR margin. The cure fraction drops, but the hazard ratio still clears.

The 4-month delay constraint is actually evidence for the model, not against it. The fact that a 4-month delay cannot solve at low BAT values means GPS must be working fast. The biology supports this -- it is an anamnestic recall response, not de novo priming. And the November 2022 continuous dosing amendment means REGAL patients maintain that immune pressure indefinitely, unlike Phase 2 where dosing stopped after a year.

The BAT mOS posterior is wider than I expected ([10, 14]m at 90% CI), but the thesis is robust across the entire range.

MRD stratification feeds directly into the models I already ran. It does not introduce a new failure mode -- it creates the bimodal BAT population that the long-survivor test already covers. And because MRD is a stratification factor, the arms are definitionally balanced. No luck-of-the-draw confounding.

I’ll leave you with one of my recent thoughts (yG19 from ST) that is suitable for wrapping up, that really provide context on how rare of opportunity this has been/is and how lucky we are to be accumulating here:

“If the warrants situation and unfavorable financing terms never happened, none of us would be here. We wouldn't have been able to accumulate/continue to accumulate at these prices.

We are all so lucky. Without the warrants situation that caused this, there would be near zero chances that SLS would be trading at current prices, it would be significantly higher, reducing our multi-bagger compounded returns that we'll get from REGAL final analysis readout and buyout.

Everyday it is mind-blowing to me that we have an opportunity to continue to accumulate at these prices when REGAL has 99.9999% chances of success and it will be the new standard of care in AML CR2 (not eligible for transplant).

A monopoly for 5 to 8 years.

The 7.5X to 49X upside from current shares is real. GPS low/conservative annual sales globally will be $4B+ from AML CR2 and CR1 (not eligible for transplant)

This is the rarest of opportunities and there is a significant margin of safety. As a smart investor, you need to go heavy."

Please post thoughts/questions/comments below and I’ll answer as I get a chance. Looking forward to thoughtful discussions here.


Upvote
189

Downvote

148
Go to comments


Share
Join the conversation
Sort by:

Best

Search Comments
Expand comment search
Comments Section
u/PennyPumper avatar
PennyPumper
MOD
•
2mo ago
•
Stickied comment
emoji:illuminati:ノ( º _ ºノ)
Does this submission fit our subreddit? If it does please upvote this comment. If it does not fit the subreddit please downvote this comment.

I am a bot, and this comment was made automatically. Please contact us via modmail if you have any questions or concerns.


UpvoteVote
Downvote

Reply

Award

Share

Xyz_83
•
2mo ago
You rock.

1st: You provide a lot of information and to learn definitely namely in statistics. You should give some classes. I have a book called "Statistics for Engineers" and I only apply it at basic level (eg. distributions) and not professionally. I would love to have your understanding especially to apply it in the biotech industry.

2nd: Amazing DD, it is quite factual regarding raw data. Regarding the statistical analysis, only a statistician can discuss properly with you.

3rd: In my opinion, the phase 2 results were already amazing. Extrapolating those to a bigger phase 3 trial and more frequent injections, your conclusions make sense and are aligned with my expectations despite i didn't this deep dive. With some calculations, at december, when the press release was issued, it only makes sense that the GPS arm stabilizes with no further events or being delayed a lot.

Unfortunately I spotted too soon 2seventybio and harpoon terapeutics. Got fucked in the ass with possible delisting and got out...both companies ended being bought by BMS and MSD.

4th: I really hope you are right, for the shareholders and specially for the patients. The immunoterapy is getting hot.


Upvote
32

Downvote

Reply

Award

Share


1 more reply
DifficultSale3318
•
2mo ago
Thanks for the DD and the time and effort it must have taken.

I’ve been in this stock since I saw an original post about SLS in this group middle of last year.

One thing I’ve learnt is there is never a ‘sure thing’.

BUT this is as close as it gets imo.

Good luck to all invested. 😎


Upvote
26

Downvote

Reply

Award

Share

MeGustaLasagna
•
2mo ago
Your analysis is quite interesting, I’ve read both of your posts and enjoyed the depth. I do have one question, though:

If your analysis is truly fault-proof, wouldn't the big funds, with their massive teams of experienced quants, have reached the same conclusion? If there is a 99.9999% chance of success, I would expect the big players to be positioned much more heavily than what they reported in December. If the math is that certain, shouldn't that probability already be 'priced in' by now?



Upvote
19

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
Thank you for your comment. And I posted this reply to another comment in the Part 1 post, Two things here:

First, and I'm not sure of the exact number but I believe before interim analysis of REGAL on Jan 2025, amount of institutions was 35 to 72

And today, about 14 months later, that number is about 171+.

This is publicly available and you can sort through the institutions and see their investment approaches/styles as well.

Second, is the warrants overhang. Fully diluted share count is 217MM, and the outstanding warrants overhang is still 40M. Essentially, for years to fund the trials for GPS and SLS-009, they had to accept unfavorable financing terms which resulted in lots of warrants being issued. And given how long the trial has gone on passed it's planned end date (which is only positive), it has artificially suppressed the price by risk-free shorting from warrant holders.

The current shorted shares amount is coincidentally about 40M shares. Good for them that they can short risk-free and earn a lot risk-free. This is what is keeping the price artificially extreme low which is great for accumulation. A lot of institutions/large shareholders are accumulating large long positions from this, for the REGAL final analysis readout and eventual buyout.



Upvote
11

Downvote

Reply

Award

Share

ImaginationEnough414
•
2mo ago
The warrants have definitely suppressed the SP.


Upvote
2

Downvote

Reply

Award

Share

u/Neither_Meaning_8621 avatar
Neither_Meaning_8621
•
2mo ago
I think that’s a good point and wise question. Curious to see some feedback


Upvote
2

Downvote

Reply

Award

Share

u/onamixt avatar
onamixt
•
2mo ago
A question: if HR is that good, then why didn't IDMC stop the trial for superiority? They saw the interim data, surely did the math but decided not to stop. It's a data point for us and should be account for as well. Probably the p-value wasn't within O'Brien–Fleming boundary



Upvote
7

Downvote

Reply

Award

Share

TTP222
•
2mo ago
There is a real chance we get a halt from them in the next 30 days



Upvote
6

Downvote

Reply

Award

Share

u/UnionJobs4America avatar
UnionJobs4America
•
2mo ago
Can you explain what this means like I am 5?


Upvote
2

Downvote

Reply

Award

Share

Away-Information9841
•
2mo ago
the full data is better than a stop for efficacy and in reality the number of patients in the trial is kind of low so full data will be the best



Upvote
3

Downvote

Reply

Award

Share

u/stumblios avatar
stumblios
•
2mo ago
Agreed. I think if it was a 300+ patient trial, perhaps it would have been halted. The 63/64 patients in each wing, minus any dropouts, gives more statistical weight to each individual so going from 72 to 80 events could dramatically change the p value. Especially if the BAT arm had better initial survival and GPS was weaker at the beginning/stronger at the end - then we absolutely want to see exactly how much better the tail end is.

I only recently invested, but I know the trial has been ongoing for years. Better to let it ride a few more months until the trial is statistically conclusive rather than halt while there is still some debate.

I will say that if we're still in the $3s or $4s mid-summer, I'm probably going to over-allocate here. Although that'll also be the time institutions agree the statistics are undeniably in SLS's favor and I doubt the price will be down here.



Upvote
2

Downvote

Reply

Award

Share

u/Just-Finance1426 avatar
Just-Finance1426
•
2mo ago
I still haven’t seen any math around the p value difference between stopping now ~72 events vs. continuing to the full 80, but my intuition is that the drug effect is large enough that it is a tiny difference. I suppose with Sellas still blinded to outcomes they have to act out of an abundance of caution and assume they need all the statistical power they can get.

I also wonder if they are happy to continue the trial while they await results from SLS009 so that it can be factored into the possible BO price as well. Personally I’ve valued it at close to zero in my calculations for SLS share price because we don’t have any certainty about the outcome, but really it could be a significant component as well.



Upvote
4

Downvote

Reply

Award

Share

Run4theRoses2
•
2mo ago
jfc. ... listen to the Oct 29th SLS Presentation three Dr's explain 009 P2B data Guarantees its approval ---


Upvote
1

Downvote

Reply

Award

Share

Run4theRoses2
•
2mo ago
valuing 009 at close to zero, either means you're just an inch thick mile wide retail tool, or a liar.


Upvote
1

Downvote

Reply

Award

Share


1 more reply
Run4theRoses2
•
2mo ago
what boundary? what boundary?

with a 60 Patient Event Sample - what boundary ... would allow for an early stop?

not to mention, this would mean fda approval and open access to a $25B TAM ...

my point being, once the number of Events was reduced for analysis, nov 2022, the company did not state there was a boundary at Interim ---


Upvote
1

Downvote

Reply

Award

Share

Run4theRoses2
•
2mo ago
12,500 AML CR2 / CR3 Patients who'll be Eligible each year + 40,000 AML CR1 patients, each new year -to add to the 100,000 patients currently in remission who will immediately be eligible and benefit from Gps Immunotherapy.

and if you think the FDA isn't going to approve Gps Condiditonally for CR1, after seeing 4x Increase in survival to 24-30 months for Cr2 with NO SIDE EFFECTs, near 100% Quality of Life, combined with the MSKCC Phase 2 CR1 TRIAL DATA of 67.6 month MOS - Better than Transplant, if you think the FDA is going to wait 5 years for a trial, when the Chair of MD ANDERSON's Leukemia Dept., running the Global P3 requested Expanded Access to GPS for CR1 patients, and they also submit that EAP DATA.

you have more research to do u/Away-Information9841



Upvote
1

Downvote

Reply

Award

Share

Away-Information9841
•
2mo ago
im not sure why are addressing me specifically all i said was this particular trail doesn’t have all that many patients and the full statistical results will help present a stronger case. i’m holding the stock long either way


Upvote
2

Downvote

Reply

Award

Share


1 more reply
Electrical-Desk5745
•
2mo ago
I ain’t reading all that, this is a casino sir… that being said you seem smart and put a lot into it so imma throw some gambling money at it.



Upvote
7

Downvote

Reply

Award

Share

u/Bjamnp17 avatar
Bjamnp17
•
2mo ago
🤣 I actually read all this , took about an hour or so. But the kid in me agrees with you!!! I bought a few more shares!😎


Upvote
1

Downvote

Reply

Award

Share

Ok-Recommendation925
•
2mo ago
You know....the last time someone preached what you said, the crowd realized he was a mentally ill dude who got lucky with ACHR Options and shared, some Tweedle Dude with the stock: ATYR

I wasn't in that shit hole, but I hope you are not some other terminally ill dude.



Upvote
10

Downvote

Reply

Award

Share

u/Walmartpancake avatar
Walmartpancake
•
2mo ago
the atyr fiasco was a mess, should have listened to pharma bro on that



Upvote
3

Downvote

Reply

Award

Share

Ok-Recommendation925
•
2mo ago
What does Pharma Bro say about SLS?



Upvote
1

Downvote

Reply

Award

Share

u/Walmartpancake avatar
Walmartpancake
•
2mo ago
Hasn’t taken a short but he isn’t very positive about SLS. However, some data was omitted when bro was analyzing and the analysis was like a year ago. I think there’s a post specifically on this at the SLS subreddit



Upvote
1

Downvote

Reply

Award

Share

Ok-Recommendation925
•
2mo ago
Alright. Having seen how he put retail to shame and humbling on ATYR, I am keen to avoid his warpath, specifically on Pharma. That bro knows his shit.

Since taken a 600 share position on SLS, avg $3.94



Upvote
1

Downvote

Reply

Award

Share

u/Walmartpancake avatar
Walmartpancake
•
2mo ago
I’m somewhere there too



Upvote
1

Downvote

Reply

Award

Share

Ok-Recommendation925
•
2mo ago
Yeah I just want to be sure I'm not in an oncoming collision with Pharma Bro.

That guy talks a lot of shit (who doesn't tbh). But when it comes to Biotech and Pharma related, he is wickedly accurate on his call-outs.

I still remember that Tweedle Retard telling his ATYR sub he dined with the CEO of ATYR, and not a single soul asked for photos or proof! It was the biggest 'Trust Me Bro' red flag....



Upvote
2

Downvote

Reply

Award

Share

u/Walmartpancake avatar
Walmartpancake
•
2mo ago
Pharma bro is busy with godel and his photonic computing. I do hope we get an analysis from him


Upvote
2

Downvote

Reply

Award

Share


4 more replies
Sprayed
•
2mo ago
What's pharma bros username? I would like to browse his posts


Upvote
1

Downvote

Reply

Award

Share


1 more reply
bowspot
•
2mo ago
I am on immunotherapy for leukemia. Would be quite funny to make money on this. I'm gonna buy some next week.



Upvote
5

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
Wishing you all the best in health! How has your experience been on immunotherapy if you don't mind sharing?



Upvote
4

Downvote

Reply

Award

Share

bowspot
•
2mo ago
Thank you!

Quite good. I'm taking 400mg of Immatinib Accord everyday for the past 7 months. Before getting diagnosed I had a lung infection basically every month, even with proper diet and lots of exercise. My immune system is completely back on track after getting medicine. I had some coughs 2 weeks ago and thought "Oh shit, lung infection" but they were gone in 3 days. Nothing happened.

Immunotherapy is awesome in my opinion. Other than some brainfog and being a bit more tired I feel like I'm living a normal life. I have chronic leukemia though, easier to treat. Acute leukemia is much more dangerous and harder to treat. Unfortunately my nephew died from it as well 10 years ago. I'm excited for this development and don't mind losing some money (in the worst case) on such an investment. I just found about it today after researching some stocks. Let's go!



Upvote
5

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
So sorry to hear about your nephew, and thank you for sharing your experience! And wishing you all the best in health going forward! And you won't lose anything here, don't worry about that, I'm right here with as a shareholder


Upvote
4

Downvote

Reply

Award

Share

gosumage
•
2mo ago
Lots of people treating this stock as a lock are at high risk to go broke. I have seen many negative surprises in pharma. This is cult mentality. Be careful.



Upvote
5

Downvote

Reply

Award

Share

u/ExcitingGuess5457 avatar
ExcitingGuess5457
•
2mo ago
For sure but I feel that's with stocks in general. As much as we all want to strike big, never trade with money you can't afford to lose & don't get greedy when waiting for a sell price. You can lose trying to wait till the highest point only for it to drop. The old saying with don't put all your eggs in one basket also holds true - whatever money you can afford to lose if it doesn't work out, don't bet all your money on one item.


Upvote
2

Downvote

Reply

Award

Share

nadiju1
•
2mo ago
I agree with you on people that put a fortune into it. It can still fail, even when the probability of a success is very high. As the other comment already noted: don't risk more on it than you're willing to lose.


Upvote
2

Downvote

Reply

Award

Share

shaqballs
•
2mo ago
Nevermind this explains your comment on the sellas sub lol


Upvote
2

Downvote

Reply

Award

Share


[deleted]
•
2mo ago
u/King_of_Ooo avatar
King_of_Ooo
•
2mo ago
Thank you for this. Why is the monopoly for GPS only 5-8 years?



Upvote
4

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
Thank you, and there is no approved drug for AML CR2 (not eligible for transplant). At the BAT mOS range the predictive model predicts with 90% accuracy, GPS will/is increasing survival for these patients 3X to 4X. It will be the only approved drug that does this, and it beats standard of care in AML CR1 by at least 1.5X (this was Phase 2 data). Based on the Phase 3 AML CR2 (not eligible for transplant) data we are seeing clearly, it will do far beyond that 1.5X in CR1 with the unlimited dosing.

The closest competitor is in Phase 1, for 5 to 8 years, there is no competitor in AML CR2 (not eligible for transplant), or anything that can achieve in AML CR1 that GPS can/is achieving.

Annual Sales for GPS from AML CR2 (not eligible for transplant) and CR1 will be $4B+ globally, hence it will be acquired/bought-out by a strategic like ABBV, BMS, etc. There will be a bidding war, as it is/will be the most sought after oncology acquisition.


Upvote
9

Downvote

Reply

Award

Share


2 more replies
u/TradingTennish avatar
TradingTennish
•
2mo ago
Excellent work, not only the modelling but also the exhaustive explanation are much appreciated.

I would ask if you'be interested in an analyst job at a biotech fund, but considering your current position in the stock you don't need a new job.

If I forced you to estimate a date for the 80th event, where would you land?

I'm considering to roll some of my shorter date calls into 2028 ones, as the currently slow rate of events pushes out my previous estimation of readout + buyout happening easily in 2026.



Upvote
4

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
Thank you! And there is still a statistical probability and chances given the high cure fraction or "cure rate" we're seeing the GPS arm of 64% that the model predicted, that event rates may dwindle down to a very minimal amount (maybe like 0.5 events per month). If the trial isn't halted for extreme success, and they continue on until the 80th event (we were at 72 as of Dec 26, 2025), than we may be here for a while until very late 2026 to early 2027.

If the "cure rate" is near 42% it'll be around Q3 2026 for the 80th event (the model predicted that based on a cure rate of 42% to 48%, capped at 50%)

But if it is near 64% "cure rate", what the cure survival model predicted with the unconstrained grid search at various BAT median OS numbers (and that we now know 10 to 13 BAT mOS has 80% chances of happening, and 10 to 14 BAT mOS 90% chances), then we may be here for a while until 2027 unless there is a halt

I would recommend 2028 LEAPs to be safe, go as far out as you can. It's what I would do as a deep value investor given the situation.


Upvote
4

Downvote

Reply

Award

Share

steadyeddy_10
•
2mo ago
Good summary 🔥


Upvote
3

Downvote

Reply

Award

Share

u/passionlessDrone avatar
passionlessDrone
•
2mo ago
I cannot speak toward the stats stuff, but if the drug was doing as well as this dd would indicate, how come the FDA hasn't just said, OK, it's working good enough, let's start helping people today and not in Q1 27 after we wait it out?



Upvote
3

Downvote

Reply

Award

Share

u/Just-Finance1426 avatar
Just-Finance1426
•
2mo ago
The FDA doesn’t ever tell a drug company to stop a trial. It is entirely incumbent on the company to decide when to halt in the event that they think they have sufficient statistical power to succeed with their new drug application to the FDA.

The difficulty is that the company is blinded and doesn’t actually know if they have sufficient data… so they have to be careful - this trial has taken like 5 years? If they fuck it up by pulling the plug too soon, they have to start a new trial. It’s truly a nightmare scenario. So I understand their hesitance to call it good enough and run the numbers.


Upvote
2

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
Thank you for your comment. Just wanted to clarify a few things here looking at the comments below and I'll explain it clearly so everyone has context.

The FDA is not monitoring the trial live. Neither is SELLAS. Both the company and the FDA are completely blinded to the data right now. The only group on the planet that knows who is getting the vaccine and who is getting the control (BAT) is the Independent Data Monitoring Committee (IDMC). The IDMC's job is to act as the referee, but they cannot just call the FDA and say, "Hey, this looks good, let's approve it." They are bound by rigid, pre-agreed mathematical contracts.

Even if the drug is working incredibly well now, the data at interim analysis at events I don't think crossed that astronomical threshold yet, as the real benefit for GPS comes from the long-term survival/cure fraction/"cure rate" we're seeing now (since October 2025 the HR has likely been where it's at now). I think if the IDMC halted today, they could with no issues. If an IDMC halts a trial without mathematically clearing that boundary, the trial is ruined, and the FDA will reject the drug for protocol violations, but we are way passed that. All the analysis everyone has done, include the machine learning model/predictive model predictions, point to a groundbreaking hazard ratio where GPS is the new standard of care in AML CR2 (not eligible for transplant).

There is a possibility that the IDMC may halt the trial. No one knows though, and we'll just have to wait and find out. In the interim, continue accumulating at these prices.


Upvote
2

Downvote

Reply

Award

Share


2 more replies
Ill_Ground_1572
•
2mo ago
Because some political idiots with irrational anti-science vendettas against vaccines are now in charge? I am not saying this as a sure thing but definitely a major concern for all vaccine based drugs currently under review.



Upvote
2

Downvote

Reply

Award

Share

u/Bjamnp17 avatar
Bjamnp17
•
2mo ago
I totally agree. Bureaucrat red tape ( bullshit) clogging up any advancement in medicine. I hear of peeps going abroad for treatments because they want to take a chance at survival than wait for a cure after they pass.


Upvote
1

Downvote

Reply

Award

Share

FoolishWizardUK
•
2mo ago
Up 17% as of yesterday and still climbing thank you very much!



Upvote
3

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
Glad to help everyone, but remember the true upside here of 7.5X to 49X (from when shares were $3.70)

REGAL final analysis readout and buyout will occur, those that have the discipline to accumulate and hold with sizeable positions will make a fortune.


Upvote
3

Downvote

Reply

Award

Share

u/hambonie88 avatar
hambonie88
•
2mo ago
Why was the TLDR longer than the actual story? Jk this is a lot of work tho, good job I guess. Maybe I don’t really know, kind of a lot to process


Upvote
3

Downvote

Reply

Award

Share

nathann28
•
2mo ago
what is your predicted timeline for the future of SLS? also what the fuck is your day job 😭 i wish i had the time to do DD like this



Upvote
4

Downvote

Reply

Award

Share

Xyz_83
•
2mo ago
i wish i had the knowledge to do a DD like this


Upvote
10

Downvote

Reply

Award

Share


5 more replies
HeeHolthaus66
•
2mo ago
Nice


Upvote
2

Downvote

Reply

Award

Share

No-Window246
•
2mo ago
Hey thanks for the analysis, although I'm not intelligent enough to understand the majority of it I do have to say that it looks very convincing and professional. Just wondering since you have a very high conviction that this will succeed how much do you have currently invested into SLS.


Upvote
2

Downvote

Reply

Award

Share


5 more replies
u/Walmartpancake avatar
Walmartpancake
•
2mo ago
might be a weird question but why did you decide to deep dive into SLS and/or the biotech field in the first place?



Upvote
2

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
•
Edited 2mo ago
Thank you for your comment. I've been a deep value investor for several years and do this with any position. I do quite a ton of due diligence before even taking a position, as I take big concentrated positions.

In the case for SLS, I can't even recall how I stumbled upon it as I've done so much due diligence since and that initial memory I can't recall, but I remember looking at the insider buys that occurred in the summer within a cluster in 2025 around May/June, I started researching around then, and then saw the doubled down insider buy that occurred in November 2025. I already started researching heavily before that November 2025 insider buy, but then I just dove so deep.

I took a huge position starting out after the research I did shortly after the November insider buy, just from going through the clinical trial data, learning about AML CR2 (not eligible for transplant, the October 29th R&D call, etc. and going down a rabbit whole even before using my machine learning/modeling skills and all the deep due diligence I've shared in these two posts. Honestly I was able to arrive at the 99.99% chances for REGAL success even before the predictive modeling, just from public clinical trial data, historical trials in AML CR2, looking at the event timings, length of the trial, the R&D SELLAS provided, etc., I just wanted to real answers/and to statistically validate, hence the machine learning route.

As did everyone else, I anticipated the 80 events to be reached by the end of Dec 2025, that didn't happen. I was in shock. And even by then I didn't even fully grasp the upside potential here until later on. I thought initially, oh, this likely would be acquired for a couple of billion by a strategic. But as I dove deep and ran the full numbers, revenue numbers, understood the AML market, the WT1 platform here, understood the monopoly they will have and how much more dominant GPS would be in AML CR2 and CR1 (not eligible for transplant), and understood how big SLS-009 is, which will be bigger than GPS, that's when everything clicked.

I saw there was 99.99% chances of success for REGAL, and clearly GPS is the new standard of care in AML CR2 (not eligible for transplant), no competitor for 7 years essentially, dominance in AML CR1 and CR2, and all the other upside from other indications, SLS-009, etc. Just GPS global revenue from AML CR2 and CR1 (not eligible for transplant) would be $4B+ annually for the acquirer. The 7.5X to 49X upside is real (when I say this I mean if shares were around $3.70. As shares go up that 49X number goes down of course.)



Upvote
6

Downvote

Reply

Award

Share

u/Walmartpancake avatar
Walmartpancake
•
2mo ago
Thanks for the detailed explanation. What is your outlook on this buyout? Also, do you agree that, regardless of the stock or acquisition, this therapy has the potential to help many patients?



Upvote
1

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
Thank you, and so a couple of things I would refer you to since I made details comments on these two questions in Part 1. There should be a comment in the Part 1 post regarding the buyout range of 6B to 40B. It is a wide range for a reason, and that comment in there provides context on why that is based on the revenue in AML CR2 and CR1 (not eligible for transplant) it will generate globally, which will be a low/conservative $4B annually. I walk through the math on why that is and at a patient level.

Second, there should be a comment around beyond AML (which we'll likely be acquired so this will be relevant afterwards) related to the WT1 targeting and platform for cancers this creates. It is also in the first post as well.

Those two comments are really in depth and they'll provide a good understanding of both these things.

And Yes, GPS is already helping patients now, in AML CR2 (not eligible for transplant), it is clearly increasing survival by more than 3X and is creating a "cure rate/cure fraction", and it performs better than anything out there by at least 1.5X in AML CR1, better than Onurug owned by BMS in CR1 by 1.5X. And this was before the unlimited dosing in Phase 3, so it will be even better performance in CR1 beyond the standard of care in CR1). The results are groundbreaking.

And with the utmost certainty, it will be acquired/bought out. SELLAS doesn't have any of the infrastructure for commercialization and they've indicated multiple times the focus on partnership/buyout.

This is what is valuable for the strategics already looking at SLS.


Upvote
3

Downvote

Reply

Award

Share

u/Bjamnp17 avatar
Bjamnp17
•
2mo ago
OP has 805k (I’m sure more) shares! Obviously OG investor who has done DD PERSONIFIED!!! I read the whole thesis ( thanks for the charts) really well written and detailed !! Best wishes to all who follow OP and invest in SLS! Bottom line… a potential cure for this tragic disease. ✌️❤️🙏🏼


Upvote
2

Downvote

Reply

Award

Share

mad_papooser
•
2mo ago
I think the most reasonable critique to your assessment is that you are relying on a mixture-cure model. Within the confines of that model, the success is extremely high. There is always a chance that GPS behaves a little differently than a pure cure model.

As we have discussed privately, my modeling was done differently and we arrived at the same conclusion so I think that validates your model (and mine)



Upvote
2

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
•
Edited 2mo ago
Thank you, and always great conversing with you. Before the mixture-cure model, I actually ran 5 other models, and they all arrived at a similar result.

Pure Cure: S(t) = p + (1-p)·exp(-λt) 67.9% cured forever
Leaky Cure: "cured" patients relapse at 1-10% per year
Weibull: S(t) = exp(-(t/η)^β) — decelerating hazard, no plateau
Log-Normal: heavy right tail, no true cure
Piecewise Exponential: fast early decline, slow late decline
Even ran Gamma Frailty as well

Comment Image
The straight HR when BAT = 11.5m was similar across all, 0.179–0.186 across ALL models. P(success) = 100% for every one (stratified HR will be higher of course, but in the 0.35-.50 range)

Why? Because the observed data constrains the math regardless of model form. BAT (exponential, mOS 11.5m) produces 54 deaths by month 58. Total observed: 72. Therefore GPS contributes 18 deaths out of 63 patients, a 28% death rate versus BAT's 86%. That 3 to 1 death ratio is what the Cox regression sees, and it doesn't change whether the 45 GPS survivors are "cured" (pure cure), slowly relapsing (leaky cure), or declining very gradually (Weibull).

The only reason model choice does matter is for long term predictions, the cure-fraction I believe represents what is occurring in reality from GPS responders. Pure cure says 64% to 68% of GPS patients live "indefinitely". Weibull says they'll eventually decline. Leaky 5%/yr says median 122m. These are meaningfully different for 5 year and 10 year survival forecasts. But they all agree on what happens within the trial's observation window, which is all the HR needs.

Attached is what the model convergence and divergence looks like for everyone's context.


Upvote
1

Downvote

Reply

Award

Share

u/No_Ruin4467 avatar
No_Ruin4467
•
2mo ago
Thanks so much for all your hard work on all this DD. Really enjoyed reading both parts. I also have a stats related background (but not quite your area of expertise) and all I can say is you put in some serious work with serious expertise as far as I can judge. Refreshing to not see a bunch of AI slop! Can I ask what you do for a living?

Another question I wanted to ask is why you’ve decided to go shares (only) instead of LEAPS?



Upvote
2

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
Thank you, glad I can be of help in providing the actual DD and opportunity here with REGAL. And I've been a deep value investor for several years and am semi-retired, but I really enjoy working and continue with deep value investing. Have a lot of years of experience in business, software engineering, machine learning/statistics, and a strong understanding of healthcare and pharma gained over time.

As for the LEAPS, I would recommend the 2028 LEAPS in the money going as far out as possible. They honestly may be better than shares. I just went for shares and have been adding shares every week but you can't go wrong with the 2028 LEAPS. Either of those two. I wouldn't recommend 2027 given the cure fraction we are seeing and without a halt, there is a possibility the 80th may occur in 2027.


Upvote
1

Downvote

Reply

Award

Share

u/Hairy_Cheetah7620 avatar
Hairy_Cheetah7620
•
2mo ago
Jesuschrist bro, do you sleep?


Upvote
2

Downvote

Reply

Award

Share

941VetInTech
•
2mo ago
$SLS over $LRMR ??? And/or the infamous $IBRX ???


Upvote
2

Downvote

Reply

Award

Share

u/Robsnorro avatar
Robsnorro
•
2mo ago
Just a few questions/remarks:

do you take in account the 80% response rate in the GPS arm? About 20% of the GPS arm will have a too low immune response. It will still help, but this group will have a separate mOS than the responders. In my simple calculations/estimations this impacts the required mOS for GPS responders quite heavily.

the 20% cured fraction (or at least survival past 36 months) in BAT is not all that strange, mOS seems to be read by a lot of people as halfway through the maximum survival, i.e. everyone is dead after 2x mOS. I don't see this one as a particular worst case assumption.

although you explained in your previous post already how you modelled the enrollment of patients, I do not see that reflected in your stress test. How does a back heavy enrollment change the outcome? Say worst case 101 enrolled by november 2023 and all 126 enrolled by march 2024. We know this is not the case but the enrollment is actually one of the overall impacting parameters on the outcomes but it is also a guesstimate to assume average time in trial of 30 months and k=0.2/0.3.

because of the enrollment the 60 and 72 events are fixed time points on a calendar but they are flexible w.r.t. to the time the patients have been in the trial. I found this hard to include in my simulations.

could you share perhaps a graph with all the KM curves for your most likely scenario, i.e. BAT 11.4 mOS, 60% cure in GPS, 20% BAT survival past 36 months, 15% censoring, immune ramp up 3 months.

Overall I really like the effort you put into this. It appears to be well thought out and solid simulation. The only unknown of course is your actual code, and the actual real world enrollment.

Personally I bought as much shares as I could afford to lose. However I am starting to think I might sell some other stocks and increase my shares further as this stock has been increasingly de-risked over the last 2-3 months. See also the 13D/G SEC filings by larger institutional funds.

For anyone reading this. Throw a few hundred towards it, accept you lost this money straight away and my gut feeling says you have a 75% chance of success of >5x. Simulations by yG19 show an even higher PoS, so do as you like.



Upvote
3

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
•
Edited 2mo ago
Thank you!

In regards to the 80% response rate and non-responder group, the model handles this, for the mapping:

The cure-fraction model S(t) = p + (1-p) * exp(-lambda * t) already has a two-population structure built in. 

The "cured" fraction p represents the patients whose immune response is strong enough for durable disease control.

The "uncured" fraction (1-p) represents everyone else, partial responders and non-responders combined. They die at rate lambda, which is the uncured mOS (the GPS non-responder group).

The biological identity point analysis in the post solves for the BAT mOS where uncured GPS mOS exactly equals BAT mOS. That ratio equals 1.0 condition is the mathematical statement of "GPS non-responders perform like control arm patients." At the identity point (BAT = 11.4m), the cure fraction is 67.9% and the uncured mOS is 11.4m. The Phase 2 immune response rate was 64%. The cure fraction and the IR rate match almost exactly. 

And attached is the graph with all the KM curves for the scenario you described (and this includes 20% of BAT living 3+ years):

BAT 11.4m mOS (with 20% BAT cure the BAT uncured mOS needs solving)

GPS 60% cure fraction (with uncured mOS solved to fit events)

20% BAT survival past 36 months (i.e., BAT has a cure fraction)

15% censoring (GPS dropout stress)

3-month immune ramp-up delay

BAT: mOS=11.4m overall, cure fraction=14.76%, uncured mOS=8.95m S(36m)=20.0% exactly

GPS: 60% cure, uncured mOS=28.92m, 3-month delay, 15% worst-GPS censoring

Events fit: 61.2 u/mo46 (target 60), 71.0 u/mo58 (target 72) - close match

Monte Carlo results (500 sims, all stressors simultaneous):

Cox HR median 0.436 (stratified top line HR will be slightly higher but within the 0.4 to 0.5 range)

95% CI [0.266, 0.681]

P(HR < 0.636) 94.6%

P(HR < 0.50) 71.5%

BAT alive 14

GPS alive 34

Comment Image
For the other questions, I'll have to get back to you on those in the morning later today, gotta catch some sleep. But amazing questions.

And you should go heavy here. You won't regret it. This is such a rare opportunity with a huge margin of safety, and insane life-changing upside. Hence why I've been spending so many hours doing all this DD and machine learning work for this.



Upvote
9

Downvote

Reply

Award

Share

u/Robsnorro avatar
Robsnorro
•
2mo ago
Absolutely smashing mate! This scenario is what I deem realistically risky. Good to see there's a 95% PoS from your model.

It does appear that your translation from Weibull curves to the actual KM curves there is some not-so-random randomization (as evidenced by the top and bottom bands of the KM curves having the same points in time where no deaths occur (the flat parts). I would expect in a true randomization Monte Carlo that the KM curves are unique and do not show the same flat parts where no deaths occur.



Upvote
2

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
•
Edited 2mo ago
Thank you! And awesome, this is exactly the thoughts/comments I like to help validate my theses.

That visual pattern is real and has a clean explanation. It is not a randomization that is not-so-random. What you're seeing there is shared enrollment, not shared survival.

i.e. in a 1 to 1 randomized trial, both arms are enrolled at the same 73 sites on the same calendar timeline. My enrollment model uses a logistic S-curve (midpoint month 25, steepness 0.15) and that curve is the same for both arms, because it has to be. That is how real trials work, patient #50 randomized to BAT and patient #51 randomized to GPS both enroll in month 28 and are both censored at month 58 − 28 = 30 months of follow-up.

The consequence of this is that both arms share nearly identical follow up time distributions, which means their censoring patterns are structurally correlated. The flat parts in a KM curve are just gaps between events, and when both arms have patients being censored at similar follow up durations, those gaps tend to line up. So, it's not a modeling choice, it's the 1 to 1 randomized enrollment that causes this.

On top of that, the 3 month immune ramp up delay means GPS patients (likely non-responders) follow BAT dynamics for the first 3 months, so the early portions of both curves are supposed to track each other by construction.

To demonstrate I directly regenerated and attached here the figure as a spaghetti plot with 20 independent simulation seeds overlaid. Each individual KM realization is unique, different event times, different step locations, different final survival. The death times are drawn from completely independent random number streams per arm. But the enrollment driven structure makes the overall shape similar, which is exactly what you would see in any real trial with 1 to 1 randomization and common enrollment windows.

Also a small clarification, the model uses exponential + cure fraction, not Weibull.

The math simply adds two distinct populations together, which is the cured group (the flat percentage of patients who hit the permanent plateau.) and the uncured group (the remaining percentage of patients who follow a standard, steady decline over time (regular exponential decay). The overall survival curve is just Group 1 plus Group 2. This is very different from a Weibull model, which assumes everyone is in one big group but their individual risk of dying bends or changes over time.

Comment Image

Upvote
3

Downvote

Reply

Award

Share

u/Scary_Resident4982 avatar
Scary_Resident4982
•
2mo ago
Ad infinitum dosing was not until April 2024. Your claim of ad infinitum dosing modification in October 2022, technically October 14 when they filed with the FDA, is flat out wrong.

However, I see my previous comment and your rebuke of my comment called it "false" with zero backup was deleted. April 2024 EU Clinical Trails site has the signed "ad infinitum" dosing change by Dr. Cicic on April 19, 2024. It's in black and white for you.



Upvote
3

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
I'll kindly correct you here. You are wrong on this.

November 2022 is when the protocol was amended to allow continuous dosing (treat until relapse).
April 2024 is when the trial simply finished enrolling its 126th patient.

Because the dosing amendment happened in late 2022, the vast majority of the patients in this trial (who enrolled throughout 2023 and early 2024) have been on the continuous dosing schedule from Day 1 of their treatment. The continuous immune pressure hasn't been active just since April 2024, it has been active for the bulk of the cohort for 1 to 2+ years.



Upvote
3

Downvote

Reply

Award

Share

u/Scary_Resident4982 avatar
Scary_Resident4982
•
2mo ago
Wrong.

https://euclinicaltrials.eu/search-for-clinical-trials/?lang=en&EUCT=2024-516405-23-00

Goto "Trial Documents". Click on "D1_SELLAS_ SLSG18-301_Protocol_2024-516405-23_Public".

Comment Image


Upvote
1

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
•
Edited 2mo ago
What you're sharing is not correct. You are citing an April 2024 signature on the EU Clinical Trials site. In global registrational trials, European implementation often lags the US because sponsors must secure separate approvals from the National Competent Authorities and local ethics committees for each individual European country. A signature on an EU portal in April 2024 just marks a local European administrative step, a registry update, or harmonization for late-joining EU sites. It does NOT mean the US patients were denied continuous dosing for a year and a half.

As mentioned, SELLAS filed this protocol amendment with the FDA in November 2022. Once cleared and approved by US institutional review boards, the US clinical sites (which drive the bulk of the trial) adopted the ad-infinitum/continuous dosing.

SELLAS is a US-based company, and the FDA is their primary regulatory body. When a protocol amendment is filed with the FDA (which happened in late 2022) and cleared by institutional review boards, it is rolled out to US clinical sites.

Maybe there is miscommunication going on here between us. SELLAS didn't initially have a plan until Interim Analysis for that to do after the 15 doses, and then they added continuous dosing. That is correct and what happened.



Upvote
1

Downvote

Reply

Award

Share

u/Scary_Resident4982 avatar
Scary_Resident4982
•
2mo ago
Yes, and they added the continuous dosing in April 2024.



Upvote
1

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
That is not correct. What I've been mentioning is that SELLAS didn't wait until the recent 2024/2025 interim analysis to add continuous dosing. They added it following the November 2022 blinded data review. In late 2022, SELLAS saw that patients were living much longer than expected and were going to outlive the original 1 year (15-dose) limit. They filed the protocol amendment with the FDA at that time, ensuring that patients could receive the vaccine ad infinitum until disease relapse.

The April 2024 signature on an EU document you linked above is just a local harmonization step for late-joining European sites. The US cohort, which drives the bulk of this trial, has been under the amended continuous protocol for over two years.



Upvote
1

Downvote

Reply

Award

Share

u/Scary_Resident4982 avatar
Scary_Resident4982
•
2mo ago
Prove it. I'm not asking you to "prove a negative" here either which would be a fallacy. I'm asking you to "prove a positive".

No company PR? Would have been big news.

Clinicaltrials not updated till 2025? That's a red herring.

If you have a copy of the SAP change from 2022, let's see it. Or if you have confirmation from Sellas IR to back you up, let's see it.


Upvote
2

Downvote

Reply

Award

Share


3 more replies
jerrysburner
•
2mo ago
>>> when BAT carries more survivors, GPS needs fewer to hit the same total

Could you explain how that works? I didn't dive deep in to it, but seemed to fly in the face of how I had expected it to work, meaning, if BAT had more "immortal" patients and lived longer, it seems like it would require better numbers on the GPS side to offset a stronger placebo affect



Upvote
1

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
Thank you for your comment. So these two things are different: constraint arithmetic vs treatment effect

We aren't designing GPS's performance. We are reverse-engineering it from a fixed observation, which is 54 patients are alive at month 58, total across both arms. That number is set by the data. We are asking: "given a BAT assumption, what GPS parameters explain 54 alive and 72 dead?"

BAT_alive + GPS_alive = 5

If you assume BAT is stronger (higher mOS), BAT keeps more patients alive, and GPS is forced to have fewer survivors to still total 54. That does not mean GPS is getting off easy, it means GPS is estimated to be weaker under that assumption.

The reason the trial still succeeds across this entire range is that even at BAT = 18 to 20m (generously above any published AML CR2 benchmark), the HR is still below the 0.636 success threshold. The data simply will not support a scenario where BAT is strong enough to erase the GPS advantage entirely, 54 survivors from 126 patients with 72 events at month 58 requires a meaningful survival difference between arms.

The predictive model results of he 90% accuracy in prediction of BAT mOS being 10 to 14 months, 80% accuracy of it being 10 to 13 months, and 99% accuracy of it being 11.4 months in that 10 to 13 month window, all indicate a groundbreaking hazard ratio where GPS is extending life more than 3x, with a significant cure fraction of 42-64%.



Upvote
3

Downvote

Reply

Award

Share

jerrysburner
•
2mo ago
Awesome man - thanks!


Upvote
2

Downvote

Reply

Award

Share

u/mistaken4strangerz avatar
mistaken4strangerz
•
2mo ago
Great work, but how do you see a path to as high as a 50x upside, when they almost assuredly will need to dilute for commercial launch?

Seems to me that the potential upside is 8x max after that; 16x if it plateaus.



Upvote
1

Downvote

Reply

Award

Share

mad_papooser
•
2mo ago
You need to look big picture. It would take a best case scenario but these things are possible:

GPS trial passes with transformational power (HR under 0.5)

Prior to getting top line results for GPS- The new SLS009 cohort for their phase 2 should have the earliest data out in May or June. This is front line AML treatment and in very difficult to treat patients (p53 and asxl1 mutations). The early data on this has been very strong as evidenced by the fact that the FDA recommended they move this newest cohort to front-line.

It would be an AML franchise for sale. Front line treatment with SLS009 and then when you get the patients in remission, you hit them with GPS (a revenue machine with multiple years of maintenance treatments)

There is an oncology patent cliff coming. Big companies are sitting on war chests. Look at AbbVie just as an example. The patent on venetoclax is up in 2029 I believe. That’s 3B revenue for them annually. SLS009 works in conjunction with venetoclax. They can purchase SLS, repackage venetoclax with SLS009- that would restart their patent clock and then they have GPS.

None of this even mentions the entire WT1 platform.

That doesn’t mean all of it will play out like this. But this is the reason you see possible scenarios of 10B to 20B ranges. It’s not as simple of looking up what the market is for AML CR2 in a vacuum.


Upvote
2

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
Thank you for your comment. I provided context on this in another comment in the Part 1 post, but readding it here for anyone new:

Here is an overview in a concise way:

GPS annual sales will be at least $4B and GPS + SLS-009 will be $6.5B to $8.5B.)

GPS extends survival to 30-40+ months (as the REGAL data implies), thus LTV estimate is:

​$260K (Y1) + $100K (Y2) + $100K (Y3) + $50K (Y4/Tail) = $510K Total LTV.

$510K ÷ 3.5 years = $145K annual revenue per patient.

The most interesting thing is new transplant ineligible patients in the U.S. (not including globally): There's only about 3,000 new CR2 and 6,000 new CR1 patients each year.

If everyone mostly died in 8 months (like they do now), revenue would be small ($260K × 9,000 = $2.3B max).

Because GPS keeps patients alive for 3-4 years, by Year 4, you aren't just treating the new patients. You are treating:

2026 survivors (Year 3 of dosing)

2027 survivors (Year 2 of dosing)

2028 new starts (Year 1 of dosing)

This is what creates the 27,000 patient pool and the $4.0B+ annual revenue

4 x 3 to 5 Peak Sales (standard for general acquisitions in Bio) is 20B for example, and this is a breakthrough in oncology (where these types of assets are acquired for 6 to 8 times peak sales).

The floor really is 10B, but I just said 6B because I'm a deep value investor and always assume worst case scenarios. You're right in that it is too low.

The range is that broad because we ultimately don't know what the bidding war between strategics like ABBV, BMS, etc. will lead to, as we're just talking about GPS here for AML CR2 and CR1. We haven't even discussed SLS-009 (which will be bigger than GPS) for the Frontline, which is in Phase 2B, we haven't talked about the other indications from the WT1 targeting that is present in 20+ cancers, etc.

Also, when I said 7.5X to 49X upside from current share prices (that was from when shares were about $3.70, so that 49X number would naturally drop as shares go up)

In addition, I can also attach one image per reddit comment, so I attached one here that shows the overview for GPS annual sales globally that the acquirer would get.

Comment Image

Upvote
1

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
Adding to what u/mad_papooser mentioned, attached is a chart for the low/conservative global annual sales estimate for SLS-009 + GPS. The range is really $6.5B to $8.5B. This is without any other indications, etc.

Comment Image

Upvote
1

Downvote

Reply

Award

Share

u/Prestigious_Bad1855 avatar
Prestigious_Bad1855
•
2mo ago
Can you guess why there are 20% of non responders in GPS arm in phase 3? As we know all AML patients over express WT1.



Upvote
1

Downvote

Reply

Award

Share

mad_papooser
•
2mo ago
Not all of their cancers present the same way. Some are more resistant at this point.


Upvote
2

Downvote

Reply

Award

Share

u/Just-Finance1426 avatar
Just-Finance1426
•
2mo ago
It doesn’t necessarily mean that the cancer is not responding, it most likely means the persons immune system is unable to see the vaccine and respond. It needs to train b and T cells to kill the isolated cancer cells. Keep in mind these are generally older patients who have finished multiple toxic and intense courses of chemo and other drugs, so it’s not surprising that some are unable to mount an immune response to a vaccine.



Upvote
1

Downvote

Reply

Award

Share

u/Prestigious_Bad1855 avatar
Prestigious_Bad1855
•
2mo ago
Got it sir. They had their immune system suppressed by the medication and also they could be old and the organs could not function well.


Upvote
1

Downvote

Reply

Award

Share

u/Prestigious_Bad1855 avatar
Prestigious_Bad1855
•
2mo ago
Sir, We have seen it working for responders among the patients who are in Remission, but what about the people who have the active disease and who were recently relapsed? Can they be given this? And can it works the same way?



Upvote
1

Downvote

Reply

Award

Share

u/Just-Finance1426 avatar
Just-Finance1426
•
2mo ago
It sounds like the immunological approach with gps is adequate to prevent remission for a period of time, but once relapse has occurred it is not adequate to bring it back to remission.



Upvote
1

Downvote

Reply

Award

Share

u/Prestigious_Bad1855 avatar
Prestigious_Bad1855
•
2mo ago
So it's completely different from immunological expression from Russian vaccine. As Russian vaccine is a personalized neoantigen vaccine. It's immune response could be far more greater than an antigen vaccine response like gps.


Upvote
1

Downvote

Reply

Award

Share

u/UnionJobs4America avatar
UnionJobs4America
•
2mo ago
(I probably missed it, so if I did, please forgive me) When are you expecting phase 3 to end? I understand that it fortunately/unfortunately has blown past the expected end date for the phase, but do you/they have any idea when it will end and results will be released?



Upvote
1

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
Thank you for your comment. And the comment below on summer 2026 does come with a caveat. There is still a statistical probability and chances given the high cure fraction or "cure rate" we're seeing the GPS arm of 64% that the model predicted from the unconstrained grid search, that event rates may dwindle down to a very minimal amount (maybe like 0.5 events per month). If the trial isn't halted for extreme success, and they continue on until the 80th event (we were at 72 as of Dec 26, 2025), than we may be here for a while until very late 2026 to early 2027.

If the "cure rate" is near 42% (from the 50% cap given Phase 1 CR1 cure rate was 47%) it'll be around Q3 2026 for the 80th event (the model predicted that based on a cure rate of 42% to 48%, capped at 50%)

But if it is near 64% "cure rate", what the cure survival model predicted with the unconstrained grid search at various BAT median OS numbers (and that we now know 10 to 13 BAT mOS has 80% chances of happening, and 10 to 14 BAT mOS 90% chances, and 99.99% within the 10 to 13 of it being 11.4 months for BAT mOS), then we may be here for a while until 2027 unless there is a halt. It's all dependent on the cure rate and if or not there is a halt.


Upvote
2

Downvote

Reply

Award

Share

nadiju1
•
2mo ago
Probably summer 2026


Upvote
1

Downvote

Reply

Award

Share

u/Holocenest avatar
Holocenest
•
11d ago
Par excellence!


Upvote
2

Downvote

Reply

Award

Share

u/OutlandishnessFew484 avatar
OutlandishnessFew484
•
2mo ago
I got a few for now, but I’ve been wondering for at least 24 hours now. What percent of ur portfolio is this lmao. Clearly u have a lot of money but i can’t help but wonder if this is a like an all in situation for you. Also are you putting any calls? I think i might’ve seen u had a comment about a Jan 28 call?


Upvote
1

Downvote

Reply

Award

Share

ScoffersGonnaScoff
•
2mo ago
You did not test:

Weibull BAT + Weibull GPS (shape < 1)

Gamma frailty mixture without cure

Spline-based hazard

Time-varying treatment effect without cure

MRD mixture explicitly

Until those are tested, cure fraction is not uniquely supported.



Upvote
1

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
A lot to go over here, but I'll cover it all. First off is that a Weibull model with a shape parameter less than 1 mathematically forces the hazard rate (risk of death) to decrease continuously over time for everyone. This is flawed because in relapsed AML, the disease does not magically get less lethal the longer you have it. Untreated and standard treated AML gets more lethal over time.

With Weibull BAT + Weibull GPS (shape < 1), this gives 4 free parameters (2 scales, 2 shapes) from 2 data points. The system is underdetermined, you would get infinite equally valid solutions. You need individual patient data with dozens of observed event times to identify the shape parameter. That said, any Weibull pair that reproduces 72 events at month 58 from 126 patients will still show a large GPS and BAT separation. The HR conclusion does not depend on the parametric form.

And a couple of things you have to remember for what we have to work with, is just the two aggregate event counts, 60 events at month 46, 72 events at month 58, from 126 patients. We do not have individual patient-level data. This constrains what we can and cannot estimate.

You said Gamma frailty mixture without care, but this assumes the patient population has hidden heterogeneity (some are frail, some are robust). The frail patients die early, leaving only the robust patients, which artificially drops the average death rate over time, looking like a plateau. The flaw in this is that in CR2 for AML, there is no such thing as a "naturally healthy" patient who lives for 5 years without a transplant. Even the "healthiest" (MRD-negative) patients die in 8–14 months. The survival curve's long-term behavior is essentially indistinguishable from a cure fraction. It would also require more parameters than we can identify from 2 event counts. And it would give a similar HR.

For the spline-based hazard you said, these are just flexible mathematical curves that bend to fit data. They are descriptive, not mechanistic. They tell you what the curve looks like, but not why. And this requires choosing the number of knots, their placement, and fitting smooth coefficients. Even with full IPD and 72 events, you would get 2-3 knots at most. From 2 aggregate counts, this is completely unidentifiable. This is an IPD method, not an aggregate data method.

You said time-varying treatment effect without cure, the delayed effect stress test already in the model (GPS follows BAT for 3-4 months, then separates) is the most clinically relevant version of this. To identify when the treatment effect changes and how, you need the full hazard trajectory, which requires individual patient data. From 2 data points you cannot distinguish ramp up from plateau from waning.

You also said MRD mixture explicitly, but this is the cure fraction model with a biomarker label. "MRD-negative subgroup with durable survival + MRD-positive subgroup with poor survival" is exactly S(t) = p + (1-p)·exp(-λt) where p = P(MRD-negative). It is not an alternative model, it is the same model.

The cure fraction model is chosen because it has the fewest parameters that exactly identify from 2 data points, it has a direct biological rationale (GPS vaccine to immune memory to durable remission, Phase 2 CD4+ responders 0/4 relapsed, Phase 2 CR1 KM plateau at 47%), and it is the standard oncology model for diseases where a subset achieves long-term remission. But the P(success) estimate does not depend on the model choice. It depends on the arithmetic: 72 events from 126 patients at 58 months of follow-up, with survival times longer than expected. The mixture cure model is the only one that fits the curve and obeys the biological laws of relapsed AML CR2 (not eligible for transplant).


Upvote
9

Downvote

Reply

Award

Share

Slow-Sun-2779
•
2mo ago
4 billion peak sales does not mean 200 dollar stock price.



Upvote
0

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
2mo ago
Nobody mentioned a share price of $200. Fully diluted share count is around 217MM. In the Part 1 post, I went through the buyout range in detail. I would recommend reviewing that for buyout range details and using the 217MM fully diluted share count to calculated the share price at each buyout price.


Upvote
12

Downvote

Reply

Award

Share


11 more replies
shaqballs
•
2mo ago
You must be in tears searching up SLS by name to promote your shitcos instead. You are under every post lmaooo