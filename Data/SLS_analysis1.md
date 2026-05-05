Hey everyone, get ready for some deep due diligence.  For context, I’ve been a deep value investor for several years.  I own 805K shares here (and am continuously accumulating every week).  I’ve done over a thousand hours of DD cumulatively, and I wanted to share the cure rate model I coded and built. 

From the over a thousand hours of DD I’ve done, before even this cure survival/rate model, I actually arrived at almost the exact same conclusions the model has predicted, from just reviewing clinical studies, trial data, AML CR2 (not eligible for transplant) trials/survival data, etc.  All roads of DD have pointed to the same conclusions.

For anyone new, here are pre-read DD resources I would recommend (as what I'm about to go over is really deep due diligence for the REGAL trial and where we are at now 5 years into the trial):

First, my stocktwits posts.  Have posted tons of DD over the past few weeks, and I feel they are very valuable for people/shareholders/new people that want to learn.

User is yG19 and can be found on the SLS Stocktwits thread

Second, this post from another reddit user is great and provides a wonderful intro to SLS (Sellas Life Sciences):
https://www.reddit.com/r/pennystocks/comments/1q133si/sellas_lifesciences_cancer_moonshot_in_the/Getting started now, I built a cure rate model (or cure survival model) for the REGAL trial (the Phase 3 trial for GPS).

And when I say “cure” here, I don’t mean “cured.”  The model is predicting how many patients who have crossed the 'Hazard Horizon.' In AML, if you survive past a certain point without relapsing, your odds of survival skyrocket.  Meaning by “cure”, it is essentially the count of GPS responders who are still alive and stable, and effectively ‘safe’.  The model is predicting that 42% to 48% are alive and in this ‘stable and effectively safe’ category.  I’ll explain more on this later from the model results.

TL;DR (although I would suggest reading all of this and the model results, it is really helpful due diligence):

SELLAS Life Sciences ($SLS) is running REGAL, a Phase 3 trial of GPS vaccine in AML patients in second remission (CR2), that are not eligible for transplant. 126 patients, 63 per arm.

72 of 80 required events have occurred as of Dec 26th, 2025. Thus, 54 patients are still alive at month 58. Only 12 died from Jan 2025 to Dec 26, 2025 out of 66 at risk.

My model says 42-48% of GPS patients will never relapse and die from this disease (once again, not literally, but where they are effectively “safe”). Not "longer survival,” but a functional cure. The math doesn't work any other way.

Expected topline hazard ratio: 0.35-0.50. Trial threshold is 0.636. Actual straight hazard ratio will be 0.31 to 0.38 (the model predicts this).  But stratified proportional cox hazard ratio at readout will be 0.40 to 0.49, as it will be "penalized" by the first 6–9 months of the trial where the curves likely cross or run close together (before the GPS immune response kicks in). Even though the tail is amazing, the early data drags the average up. The hazard ratio results will be a blowout, and it will be new the standard of care in AML CR2 (not eligible for transplant).  It will be a monopoly for 5 to 8 years with zero competitors (as the nearest competitor is in Phase 1). The theoretical long-term tail HR is even lower (about 0.13), but early non-responder deaths on the GPS arm will pull the headline number up to the 0.35-0.49 range. Which is still a blowout/landslide.

I tried to make this trial fail in the model. I couldn't. BAT would need mOS > 23 months to kill the result. No CR2 AML population has ever gotten past 18 months (and when I mean 18, that is like the highest outlier ever).  Modern BAT mOS in AML CR2 (not eligible for transplant is and will be 8 to 12 months, plenty of data and clinical studies show this, and doctors verify this as well from what they see when treating patients)

Even the conservative model -- which assumes BAT is performing 30% above historical norms -- still shows a 64% cure fraction. I triple-checked the enrollment curve, the denominator, and the late-trial hazard rate. Every check strengthened the bullish case.

Now, getting started into the model results:  The deceleration signal
I've done over a thousand hours of DD and have stared at the REGAL event data continuously.

Here are the facts from SELLAS's public disclosures:

As of December 29, 2025, SELLAS reported 72 of 80 required events, with the IDMC recommending the trial "continue without modification" at both interim reviews.

Sixty events by December 2024. Then... only 12 more deaths in the next 12 months, from 66 patients still at risk.

That's an event rate of about 1 per month. Early in the trial it was running at 2+ per month.

Events are decelerating. That pattern is the core evidence.

r/pennystocks - $SLS (Deepest Due Diligence for REGAL Trial) (From a Deep Value Investor)
In a normal trial where both arms are dying at a steady rate, you'd expect events to keep coming at roughly the same pace (or even accelerate as the sicker patients catch up). That's not what's happening here.

The ONLY mathematical shape that explains 72 events at month 58 with this deceleration pattern is a cure-fraction model on the GPS arm.

I explained this above, but I want to emphasize this again here, what do I mean by "cure"?
I know what you're thinking. "Cure" is a loaded word. Let me explain what it means mathematically, because this is the whole thesis.

In survival analysis, there's a model called a cure-fraction (or "mixture cure") model. It splits patients into two groups:

Cured patients -- their risk of dying drops to basically zero. On a survival curve, they flatten out into a permanent plateau. They never come off the curve.

Uncured patients -- they follow a normal exponential decline. They eventually die, but with a measurable median survival.

Why did I use this model instead of a standard one? Because a standard exponential model can't explain the data.

Think about it: we have 72 deaths at month 58. If everyone on both arms was dying at some steady rate, you can calculate what those rates would be. But the pattern of those deaths matters. The early deaths came fast. Now they've slowed to a crawl. Twelve deaths in twelve months from 66 at risk.

A standard model where everyone keeps dying at the same rate would predict WAY more events by now. The only shape that fits is one where a chunk of patients stopped dying entirely.

That chunk is the cure fraction. And my model says it's about 42-48% of the GPS arm.

I didn't assume this from Phase 2 data. I reverse-engineered it from the 72 event count and the deceleration pattern. The cure fraction is the output, not the input.

Now onto explaining the model
Here's what fits the data:

BAT arm: Exponential survival, median OS = 10 months (consistent with historical CR2 AML and the venetoclax era) (and don’t worry, as you’ll see later on, I tested all the way up to a BAT mOS of 23 months)

GPS arm (cure-fraction model):

Cure fraction: 42-48% (these patients plateau and never die)

Uncured median OS: 34-39 months (even the "uncured" GPS patients live 3x longer than BAT)

GPS theoretical mOS: 97-183 months (yes, that's 8-9+ years -- because the median is pushed way out by the cure plateau)

r/pennystocks - $SLS (Deepest Due Diligence for REGAL Trial) (From a Deep Value Investor)
Look at that blue curve. It doesn't go to zero. It flattens. That plateau at about 42% is 27-30 patients on the GPS arm who, according to the model, are “cured” (or stable and safe, not in any danger at all of relapsing).

The BAT arm (red) follows a clean exponential. Median survival ~10 months. By month 58, almost all of them are dead.

The statistical constraints
This section addresses the strongest counterarguments.

I showed you the model above with BAT=10m and a 42% cure fraction. That's the "anchored" version, I pegged BAT to historical norms and let the math figure out the rest.

But what happens if I take the training wheels off? What if I let the model freely choose BOTH the BAT mOS and the cure fraction simultaneously, with no historical anchoring?

The result is more favorable to GPS, not less.

The unconstrained grid search pushed BAT all the way up to 14.5 months -- about 30% above historical norms -- because the events are coming in so slowly that even the Control arm appears to be outperforming. Crucially, even with that inflated BAT baseline, the model STILL spits out a 64% cure fraction on GPS.

r/pennystocks - $SLS (Deepest Due Diligence for REGAL Trial) (From a Deep Value Investor)
That chart is the key to this entire section. It shows the mathematical relationship between the assumed BAT mOS and the required GPS cure fraction to produce exactly 72 events at month 58. It's not a choice, it's a constraint (this is actually what happened, as of Dec 26th, 2025). The 72 event count pins you to that curve.

Why the cure fraction is a structural requirement: Because the model sees the Control arm doing so well (14.5m), the only way the Drug arm can STILL be winning, which the event deceleration implies, is if the Drug arm has a massive "tail" of long-term survivors. The high cure fraction isn't optimistic fluff; it's the mathematical counterweight required to balance the high BAT mOS.

The 11-month reality check: If we anchor the model back to the real-world historical BAT mOS range (say 10-11 months instead of the model's inflated 14.5 months), the implied efficacy of GPS skyrockets even further. The conservative unconstrained model is actually masking the drug's true performance by attributing the slow event rate to a super-performing control arm rather than a super-performing drug. The anchored model at BAT=10m gives about 68% cure with uncured mOS of 20m. Push BAT to 14.5m and the math forces cure up to 64%.  The reason for this is simple, it’s the only way to arrive at the 60 Events as of Dec 2024/Jan 2025, and 72 Events as of Dec 26, 2025:  As you lower the BAT (make the Control arm more realistic/worse), the GPS Cure Rate increases (from 64% to 68%).

You can't have it both ways. There is a direct mathematical linkage: you CANNOT lower the Cure Fraction without also lowering the BAT mOS back toward historical norms. If you say "64% cure rate is too high," you are mathematically forced to admit "then the Control arm is dying faster than 14.5 months." And if BAT is dying faster, GPS's relative advantage gets bigger, not smaller. You can't have a low cure rate AND a super-performing control arm without breaking the 72-event count we already have.

I even stress-tested the enrollment curve. The model uses an S-curve for patient enrollment. What if I made it more back-loaded, reflecting the fact that REGAL enrollment surged after the November 2022 protocol amendment? With heavily back-loaded enrollment, BAT mOS drops from 14.5 to about 12.5-13.0 months, much closer to historical. But the cure fraction barely moves. It stays at 64%. The 14.5-month BAT finding was actually the conservative scenario. If BAT is really 12-13 months (more realistic), the model is MASKING how good GPS really is.

I triple-checked my own model
Before posting this, I wanted to make sure I wasn't fooling myself. So I ran three independent verification checks. Every single one strengthened the thesis.

1. The denominator
This sounds basic but it matters. N = 126 (not 140 as originally planned). 72 events out of 126 patients means 57.1% event maturity, we are past the pooled median overall survival. The pooled median OS (across both arms combined) is now a hard historical fact, not a projection. More than half the patients have already died. The remaining 54 are the tail of the distribution, and the GPS arm is where most of them are sitting.

2. The enrollment curve
The model uses a logistic S-curve for enrollment (midpoint month 25, steepness 0.15). I asked: what if enrollment was more back-loaded than that? REGAL had a protocol amendment in November 2022 that likely accelerated late enrollment. So I tested:

Heavily back-loaded (mid=30, k=0.20): BAT drops to about 13.0m. Cure stays at 64%.

Extreme back-loading (mid=30, k=0.25): BAT drops to about 12.5m. Cure stays at 64%.

The takeaway: even if enrollment is more back-loaded than modeled, BAT comes DOWN toward historical norms while the cure fraction stays HIGH. This significantly weakens the 'maybe BAT is just really good' argument. If BAT isn't 14.5m -- and it almost certainly isn't -- then the cure fraction is even more locked in.

3. The velocity proof (the strongest check)
This is the single most compelling piece of evidence in the entire analysis.

December 2024: 60 events, 66 alive

December 2025: 72 events, 54 alive

12 deaths in 12.5 months from 66 at risk

The math:

Hazard rate: 12 / (66 x 12.5) = 0.0145 per person-month

Annualized mortality: 16%

Implied median survival for this population: about 48 months

Now compare what you'd expect if the surviving population were following a pure exponential at different median survivals:

mOS assumption	Expected events from 66 in 12.5mo
10 months	38.3
14.5 months	29.7
20 months	23.2
30 months	16.6
50 months	10.5
OBSERVED	12
If BAT had mOS = 14.5m, you'd expect 30 deaths from 66 patients over 12.5 months. We got 12. Even an mOS of 50 months would give 10.5 deaths. The observed rate matches a population with implied mOS of ~48 months.

Early in the trial, events were coming at 2+ per month. Now it's barely 1 per month. The survival curve has flatlined. This is the cure fraction in real time.

r/pennystocks - $SLS (Deepest Due Diligence for REGAL Trial) (From a Deep Value Investor)
The Phase 2 backstory and why REGAL might be even better (very important context here)
GPS isn't new. There's Phase 2 data. And here's where it gets interesting.

Phase 2 CR1 (Maslak 2018): Patients in first remission. mOS was not reached at >67.6 months. 3-year OS was 47.4%. The curve had a famous "ghost plateau" at about 47%. Among CD4+ responders, 0 out of 4 relapsed. This was the first hint of a cure fraction.

Phase 2 CR2 (Brayer/Moffitt): Patients in second remission (not eligible for transplant) same population as REGAL. mOS = 21.0 months vs 5.4 months for control. Significant, but no plateau. No cure fraction.

So why would REGAL show a cure fraction in CR2 patients when Phase 2 CR2 didn't?

Because they changed the dosing protocol. This is the key difference.

Feature	Phase 2 CR2	Phase 3 REGAL
Dosing	6 shots, then stop	Monthly boosters indefinitely
Duration	Fixed schedule	Treat until relapse
Observed mOS	21.0 months	Modeled >60+ months
Remission	CR2	CR2
Control mOS	5.4 months	Est. 8-14m (venetoclax era)
Phase 2 CR2 showed GPS could delay death 21 months vs 5.4 months. But they stopped dosing after 6 shots. The immune response faded. Patients relapsed and died.

REGAL uses induction + continuous monthly boosters until relapse. The hypothesis: continuous boosting converts "delayed death" into "long-term immune surveillance,” basically converting the CR2 trajectory into something that looks like the CR1 ghost curve.

And that's exactly what the model shows. The 42% cure fraction in REGAL sits right next to the 47% plateau from Phase 2 CR1.

REGAL isn't inventing a new effect. It's reproducing the CR1 effect in CR2 patients by keeping the immune pressure on with continuous dosing.

The numbers: sensitivity analysis
I didn't just run one scenario. I swept BAT median OS from 8 months to 20 months. The question: how strong does BAT need to be to make the trial fail?

BAT mOS	Conditional HR (responders)	P(success)
8m	0.10	100%
10m	0.13	100%
12m	0.16	100%
14m	0.22	100%
16m	0.31	100%
18m	0.45	~99%
20m	0.61	~95%
Note: These are conditional HRs -- the benefit seen among responders on the survival plateau. While the theoretical benefit for survivors is massive (HR about 0.13), early non-responder deaths will drag the topline average to a realistic 0.35-0.49. Both ranges are safely below the 0.636 threshold, and will make GPS the new standard of care in AML CR2 (not eligible for transplant).

r/pennystocks - $SLS (Deepest Due Diligence for REGAL Trial) (From a Deep Value Investor)
Even when I give BAT a wildly generous 20-month median, which would be unprecedented for CR2 AML, the hazard ratio is still 0.61, below the 0.636 threshold. GPS still wins.

A note on what the headline HR will actually look like
Let me be straight with you here, because I don't want to oversell and lose credibility.

The model's conditional HR of 0.13 (at BAT=10m) is mathematically correct. It's the hazard ratio for the GPS responder subpopulation -- the patients who are on the plateau and never coming off. But that's NOT the number you'll see in the topline press release.

Here's why. In a real clinical trial, a Cox regression fits a single HR across ALL patients and ALL timepoints. That means the 55% of GPS patients who are NOT in the cured fraction -- who relapse and die early, get averaged in. Those early GPS deaths drag the observed HR up from the theoretical 0.13 toward something more like 0.31 to 0.49.

Think of it this way: the cure fraction gives GPS a massive late-game advantage (the flattening tail), but the Cox model also counts the early innings where uncured GPS patients are dying at a pace that's closer to BAT. The average of "terrible early + spectacular late" is "really good but not insane."

The expected topline readout HR: roughly 0.31 to 0.49.

For context on how good that still is (which it is breathtaking amazing in AML CR2 (not eligible for transplant):

Keytruda's landmark KEYNOTE-024 trial (lung cancer): HR = 0.60

Keytruda's KEYNOTE-189 (lung cancer, combo): HR = 0.49

Opdivo's CheckMate-067 (melanoma): HR = 0.55

Trial threshold for REGAL: HR = 0.636

My expected topline for REGAL: HR = 0.35-0.50

An HR of 0.40 would be considered spectacular in oncology. REGAL doesn't need to hit 0.13 on the press release to be a blowout success. It needs to beat 0.636. And even my conservative 0.31 to 0.49 estimate clears that by a mile.

I'm deliberately under-promising here. If the cure fraction is real, and the event deceleration data strongly says it is, the HR will blow through even the 0.50 expectation as follow-up lengthens and the plateau becomes more pronounced. The longer they wait to cut the data, the lower the HR goes. Time is GPS's friend.

Devil's advocate: I tried to make this fail
This is the section I want you to really sit with.

For this trial to FAIL, BAT needs to achieve mOS > 23 months. Let me put that in context:

Historical BAT for CR2 AML: 6-8 months

With venetoclax-era improvements: maybe 10-14 months at the high end

The world record for CR2 AML (not eligible for transplant) highest outlier survival with any treatment: roughly 16-18 months (hard to even find data for this, a median of this with BAT in purely not possible at all).

For REGAL to fail, the median of the BAT arm’s highest recorded surviving outliers needs to beat the world record by 5+ months. Not in a trial designed to test BAT, just accidentally, in the control arm.

r/pennystocks - $SLS (Deepest Due Diligence for REGAL Trial) (From a Deep Value Investor)
Look at the margin of safety on that chart. The entire historical range for BAT is deep in the green zone. You'd need a miracle on the BAT arm to even get close to the failure boundary.

I tried to make this fail. I couldn't.

Here's what I stress-tested:

Censoring bias (the "fake good data" check): Censoring bias is the risk that patients are dropping out of the trial early because they are sick, making the drug look better than it is.  For context,in Phase 2 of GPS for AML CR2 (not eligible for transplant), this number was 15%.  In plain terms: if the sickest GPS patients quietly withdrew before dying, and the trial only counted the healthy remaining patients, you'd get a falsely optimistic survival curve. I stress-tested this by assuming that up to 30% of "lost" patients actually died immediately after dropping out -- the absolute worst case. Result: the cure fraction barely budged, and the HR changed by less than 2%. The survival benefit is not a statistical artifact of missing data.

IDMC "continue without modification" at both interim reviews. If the arms weren't clearly separated, they would have modified or stopped. They didn't. Twice.

The 72-event count is organic. It's not driven by assumptions. The model was reverse-engineered to match it.

Enrollment back-loading: Drops BAT to 12.5-13m, cure stays at 64%. Actually makes GPS look better.

The velocity proof: From Jan 2025 to Dec 26, 2025, only 12 patients died out of 66 at risk. That's a hazard of 0.015/person-month -- equivalent to a population with median survival of 48 months. Early in the trial, events were coming at 2+ per month. Now it's 1 per month. The survival curve has flatlined. This is the strongest quantitative evidence for the cure fraction.

Where the survivors are
Before I share this, I wanted to mention that I actually arrived at around these same numbers predicted by the model, for how many BAT are alive and how many GPS are alive, after a thousand+ hours of DD, and from all the clinical studies out there, and data available for AML CR2 (not eligible for transplant).  Seeing the cure survival model predict almost the same numbers was satisfying.  As I mentioned, all roads of DD here lead to the same conclusions. The model predicts how the 54 surviving patients break down:

BAT Arm	GPS Arm
Total	63	63
Dead	~57	~18
Alive	~6 (10%)	~45 (71%)
Cured (GPS)	--	~26-30
r/pennystocks - $SLS (Deepest Due Diligence for REGAL Trial) (From a Deep Value Investor)
About 45 of 63 GPS patients are still alive vs About 6 of 63 on BAT. And roughly 26-30 of those GPS patients are projected to be in the "cured" plateau -- their KM curve has flattened, and they aren't coming off it.

Timeline
80th event (final trigger): Likely Q2 or Q3 2026

Final analysis + readout: Q3 2026

But: The trial may never hit 80 events. The asymptotic max is about 93. If the cure fraction is real, events will keep decelerating. SELLAS may trigger final analysis on a calendar date rather than waiting.

I’ll now leave you with some of my recent posts on Stocktwits which will cover some good DD and points suitable for wrapping up
Post 1: “Buyout will be 6B to 40B+ 

GPS annual sales will be at least $4B and GPS + SLS-009 will be $6.5B to $8.5B.   (Please view the tables attached)  

GPS extends survival to 30-40+ months (as the REGAL data implies), thus LTV estimate is: 

​$260K (Y1) + $100K (Y2) + $100K (Y3) + $50K (Y4/Tail) = $510K Total LTV.  

$510K ÷ 3.5 years = $145K annual revenue per patient.  

The most interesting thing is new transplant ineligible patients in the U.S. (not including globally): There's only about 3,000 new CR2 and 6,000 new CR1 patients each year.   

If everyone mostly died in 8 months (like they do now), revenue would be small ($260K × 9,000 = $2.3B max).  

Because GPS keeps patients alive for 3-4 years, by Year 4, you aren't just treating the new patients. You are treating:  

  

2026 survivors (Year 3 of dosing)  

2027 survivors (Year 2 of dosing)  

2028 new starts (Year 1 of dosing)  

This is what creates the 27,000 patient pool and the $4.0B+ annual revenue”

Post 2: “GPS 3-4X's survival (saves lives) in AML CR2 (not eligible for transplant), 1.5X in CR1 minimum, enters a market (CR2 Maintenance) with ZERO competitors. It is a monopoly from Day 1 for at least 5 to 8 years.  

BMS and ABBV will need to acquire SLS, the one that does not is screwed.  

7.5X to 49X upside from current share prices. "

Post 3: “It's incredible to think about the foresight the Sellas team had when they came across GPS in Phase 2 (for AML CR2 not eligible for transplant) at Moffitt/Memorial Sloan Kettering. They were smart, saw this would change lives for those in AML and decided this was a worthy pursuit (despite conventional wisdom at the time saying there were 80%-90% chances of failure in Phase 3 for AML CR2 patients not eligible for transplant, and it has never been done before) 

They licensed GPS, and went through tons of perseverance to raise the hundreds of millions to do Phase 3, went through delayed enrollment issues from 2020-2021, but they push on. 

While the financing terms wasn't ideal, that likely is what resulted in us being able to accumulate at these prices. 

And 5 years after the start of the trial in Feb 2021, there is now 99.9999% chances of success and it will be standard of care in AML CR2 (not eligible for transplant). 

A monopoly for 5 to 8 years. 

We're all so lucky to be here accumulating.”

Please post thoughts/questions/comments below and I’ll answer as I get a chance.  Looking forward to thoughtful discussions here.

r/pennystocks - $SLS (Deepest Due Diligence for REGAL Trial) (From a Deep Value Investor)

Upvote
357

Downvote

214
Go to comments


5

Share
Sort by:

Best

Search Comments
Expand comment search
Comments Section
u/PennyPumper avatar
PennyPumper
MOD
•
3mo ago
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


1 more reply
Ohhmama11
•
3mo ago
You had me at “Hey” all in



Upvote
144

Downvote

Reply

Award

Share

filter_me_out
•
3mo ago
😂😂😂😂


Upvote
3

Downvote

Reply

Award

Share

heloguy1234
•
3mo ago
Bro, if we see .35 HR and this thing sells for 40B I’m buying a fucking yacht and naming it GPS.



Upvote
41

Downvote

Reply

Award

Share

u/OkEngine2723 avatar
OkEngine2723
•
3mo ago
I’m naming my first kid GPS and the second 009


Upvote
25

Downvote

Reply

Award

Share


1 more reply
u/Robsnorro avatar
Robsnorro
•
3mo ago
It's late and I've had a few beers, but I seem to read from your DD that you are modeling/assuming that the patients are running into their 58th month in the trial. That may be true of a very small amount, but the largest part of the enrollment took place nearer between september 2023 (105 reached) to april 2024 (all 126 enrolled). So we can say all patients have been enrolled for minimum ~23 months and 105 out of 126 have been enrolled for minimum ~29 months.

58 months is grossly over estimating... Take those numbers in account and you end up with: say BAT 8-12 months, with a 20% tail survival beyond 24 months, then 80% GPS response rate, 20% non-responders same as BAT, GPS responders 30+% 36 month survival, then GPS responders 32+ months mOS and total GPS around 28 months mOS. Still amazing.

I'll definitively read your DD tomorrow again though ;)



Upvote
48

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
3mo ago
•
Edited 3mo ago
Catching up on comments. First off, thank you for your comment and enjoy the beers! Month 58 in the model refers to the Trial Duration (time since the very first patient started in Feb 2021), not the average patient duration. ​The model never assumed all patients were on the trial for 58 months.

Specifically tested a heavily back-loaded curve (midpoint=30, matching the late 2022/2023 surge).

The model uses an S-curve enrollment integration. Example: So, a patient enrolled in September 2023 (month 31) gets 27 months of follow-up, not 58.

The enrollment CDF at month 31 gives 81% (about 102 patients), close to the your 105 figure. The model's S-curve (midpoint=25, steepness=0.15) is well-calibrated to the actual enrollment pattern. I stress tested even more back loaded enrollment (mid=30, k=0.20) in the triple-check, BAT dropped to 13m, cure stayed at 64%.

Even with this back-loaded curve, the model still required a 64% Cure Fraction to explain the low death rate.

You also said this:

"Take those numbers in account and you end up with... BAT 8-12 months... GPS 28 months mOS. Still amazing."

The math doesn't let you do this. If it were just 28 months mOS (without a cure plateau), we would be seeing more deaths right now from the patients enrolled in 2023 (who would be hitting the 2-year mark).

We only saw 12 deaths from Dec 2024/Jan 2025 to Dec 26th, 2025.

​The care survival model proved that if you lower the BAT mOS to 11 months, the Cure Fraction goes UP (to 68%), not down. You cannot have a normal 28-month survival curve with only 1 death per month at this stage; the curve must be flat.

If it were a standard 28 month curve, the slope would still be generating 2-3 deaths/month right now from that 2023 cohort. Instead, we are seeing 1 through 2025. The only mathematical shape that fits 1 death/month this late is a flat plateau.



Upvote
29

Downvote

Reply

Award

Share

u/Robsnorro avatar
Robsnorro
•
3mo ago
Thanks mate! Great clarification and I misunderstood the 30 and 0.2 parts for the enrollment loading.

I only modelled in Excel, using Weibull and Km factors. But I end up pretty much with the same results though. I assumed 20% long tail survival for BAT, so at 72 events something like ~10-15 patients still alive at best. Probably a bit less. About 19-24 GPS patients passed away, mostly the non-responders.

And that is something you take in account which many others forget. The Cox weighted (or similar) hazard ratios will be a lot higher due to the 'bad start' for GPS since the immune system needs to ramp up and they lose the non-responders.

So even with GPS vs BAT at 28 vs 10 months mOS the HR will be higher than 0.36, more like 0.45. which is still fantastic.



Upvote
11

Downvote

Reply

Award

Share

Level_Push467
•
3mo ago
See, what a few more beers does to ya??? :)


Upvote
8

Downvote

Reply

Award

Share


2 more replies
Intelligent_Yoloer
•
3mo ago
At 10 months for BAT and 28 months for GPS, you’re suggesting an HR of ~0.36. Even with the adjusted enrollment timeline, that’s a blockbuster result. Stock will moon



Upvote
9

Downvote

Reply

Award

Share

u/Robsnorro avatar
Robsnorro
•
3mo ago
The HR isn't a simple ratio but time weighted (Cox or equivalent), so the fact that BAT and GPS have similar curves at the start (due to immune response ramping up) means that the HR is going to be higher than the 10:28 months ratio suggests. Still, a good end result below 0.5 is reasonable.


Upvote
3

Downvote

Reply

Award

Share

u/OnundTreefoot avatar
OnundTreefoot
•
3mo ago
He does try to address this with his #2: the enrollment curve.



Upvote
5

Downvote

Reply

Award

Share

u/Robsnorro avatar
Robsnorro
•
3mo ago
Yup, he explained it clearly in a reaction. Average of 30 months in the trial.


Upvote
2

Downvote

Reply

Award

Share

artsnob11
•
3mo ago
This is a ton of DD based on what I see I’m in for some shares on Tuesday


Upvote
2

Downvote

Reply

Award

Share


13 more replies
u/Ok-Function-8643 avatar
Ok-Function-8643
•
3mo ago
•
Edited 3mo ago
Thankyou very much for the time to put this DD together & for sharing, it’s greatly appreciated by the majority, I’m sure. Of course, you’ve found a few battery operated verbal dildos here with the intellect of a sponge, but, it’s reddit after all so assume you won’t be offended.

Obviously like most investors, I hope you’re 100% correct, after all we’d all love our investments to be highly successful.

But, what would be truly amazing, is if your analyses is correct, and we see this gigantic shift in survival (& comfort) rates for AML patients who are burdened with such a nasty disease.

The suffering these people, and their families, are subjected too historically is truly horrific, and incredibly heartbreaking.

So, while we all hope our lives become easier financially from SLS, the real payoff would be seeing the impact GPS could have on human life - real people, living this day in, day out.

And it’s for that reason, personally I am hoping for the IDMC to halt the trial this month & help speed this quicker into commercialisation, regardless of optimal financial timelines. The difference in time could save countless lives.

Let’s hope we are on the side of something truly groundbreaking.

Thankyou again, this DD is very informative.



Upvote
16

Downvote

Reply


1

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
3mo ago
Thank you, really appreciate your comment! In my life thus far, this was the only investment where I had a genuine feeling of "the company doing genuine good in the world." Hard to describe in words, but I've been a deep value investor for years, and every opportunity has always been about what you would expect, which is growing capital, returns, compounding, etc. While that is present here (in far greater magnitude than any other deep value opportunity there is now or that I've experienced across the years), I feel so happy for the AML CR2 (and CR1) patients that will benefit from GPS (and SLS-009). I hope everyone in the trial lives as long as possible. Even in the modeling when the cure survival model provided where it predicts the 80th event will occur, and up to the 93rd event, etc. in my heart I hope that everyone in the trial lives as long as possible, as it is such as a deadly/horrific disease that affects patients, families/loved ones.

Thank you once again for your thoughtful comment.



Upvote
3

Downvote

Reply

Award

Share

u/Ok-Function-8643 avatar
Ok-Function-8643
•
3mo ago
Exactly, well said, this is one of those few investment opportunities where the company can literally change the world for so many. The fact this stock is so heavily manipulated is pretty deplorable, but, it won’t matter in the long run. Thanks very much again for the hard work here & the reply.


Upvote
2

Downvote

Reply

Award

Share

Glass_Bad6980
•
3mo ago
Great DD, thanks for posting. I’m expecting the HR around 0.47-0.5. So for your calculations, seems like this is an upper bound for HR. Only thing I cant really explain is, why there was no efficiency halt in August. If we assume 12 events in last year happened linearly, August event number was around 66-67. For efficiency halt, we need p<0.001 though depends on the study design, which suggests a HR<0.45-0.47 around 66-67 event. August meeting was not an official interim, and I haven’t found an example of an efficiency halt in a non interim meeting in history. But still, this suggests whether the IDMC was being very conservative and didn’t really cared about the p value or the HR in August was >0.5. Another problem is, why their model was still suggesting year end for 80th event even after August meeting. If the events were linear, it doesn’t make sense to expect the 80th event in year end when you see the unblinded data in August. It might be also the company was just trying to keep up with a near term catalist story.



Upvote
12

Downvote

Reply

Award

Share

u/Basic-Guitar3066 avatar
Basic-Guitar3066
•
3mo ago
IDMC never stops the trial. When FDA said stop at 80th event, the trial stops at 80th.

In August IDMC unblinded the data but it was still blinded to the company. What are you talking about?


Upvote
3

Downvote

Reply

Award

Share


1 more reply
u/Next_Degree avatar
Next_Degree
•
3mo ago
6B to 40B+ is a really broad range for a buyout, can anyone elaborate more on this or give a more precise estimate? 6B seems way too low and id love for it to be 40B but is that too good to be true?

(ive been following SLS for a while, bought shares already, I just like hearing input. No wrong answers since nobody truly knows!)



Upvote
12

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
3mo ago
•
Edited 3mo ago
Thanks for your comment. I can expand on this but here is an overview in a concise way:

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



Upvote
14

Downvote

Reply

Award

Share

neo2551
•
3mo ago
I preditct SLS009 2B might end before REGAL. (2B might end in Q3).



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
3mo ago
Thank you for your comment. This very well could happen. REGAL is such a massive catalyst and all that we're discussing in terms of results, buyout, etc. has been based on REGAL/GPS, but if SLS-009 results come out at that timeline, which they very well could, it will be a huge catalyst as well.

For everyone's context that is new/reading this, here is an overview for what SLS-009 is:

Phase 2 for SLS-009 proved that for patients that failed Venetoclax (ABBV's drug), where they typically survive 2.5 months afterwards, SLS-009 achieved an extended median OS of 8.9 months, which is a 3.5X improvement over standard of care.

Venetoclax generates $2.5B+ in net revenue for ABBV, and SLS-009 protects that by making it effective for meaningfully longer. The combo also protects it from the patent cliff.

The Current Standard in Frontline for AML: Aza/Ven is 14.7 median OS
With SLS-009: Aza/Ven + SLS-009 likely would be 22 to 24 months median OS

In TP-53 Mutated (High Risk): Aza/Ven is 5.3 months median OS
Here, Aza/Ven + SLS-009 likely would be 15 to 16 months median OS

They'll (ABBV) gain a minimum of $2B in revenue from acquiring SLS-009. Exciting for ABBV because after Phase 2B, it can be approved by 2027 given its fast track approval and orphan drug designation.


Upvote
5

Downvote

Reply

Award

Share


7 more replies
u/Next_Degree avatar
Next_Degree
•
3mo ago
Thank you.

honestly I only read some of your DD because ive read others in the past, im already sold but im just dreaming big. This is the only stock that I don't mind the price dropping until buyout, im accumulating all that I can... so help me God!

Edit: until recently I was only considering GPS, and not SLS-009, so it makes sense the BO is unpredictable.


Upvote
2

Downvote

Reply

Award

Share


1 more reply
Legym
•
3mo ago
Nice post. I own 150k shares and 4500 call options.



Upvote
12

Downvote

Reply

Award

Share

u/I_Buy_Stock avatar
I_Buy_Stock
•
3mo ago
big boy buying. 3500 leaps for me. Great position


Upvote
5

Downvote

Reply

Award

Share

u/Supernova-84 avatar
Supernova-84
•
3mo ago
Excellent analysis. Very similar to thoughts and research I have done so it’s nice to see this so well laid out. I agree with all of it.

One thought I had while reading your post is regarding the unlimited dosing. In your chart, you assume 1.4 and 1.1 events per month in 2025. If unlimited dosing began in May 2025, perhaps the event per month figure has collapsed even further from that point forward. Could we be in the 0.5-1.0 events per month range now. Meaning 80th event could come July 2026 or as far out as let’s say March 2027.



Upvote
11

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
3mo ago
Thank you! And Yes, you are correct in regards to the unlimited dosing as of May 2025.

You're right that the event rate didn't just stabilize, it went downwards because the patients who would have relapsed in late 2025 got extended life by the unlimited dosing.

I've believed this as well even before the cure survival model. The 1.1 events/month to what you mentioned of 0.5/month is likely the direct result of this May 2025 unlimited dosing and the model supports this as well. We may legitimately never reach the 80th event, or not reach it for a while.



Upvote
4

Downvote

Reply

Award

Share

u/ProfessionalDesk1914 avatar
ProfessionalDesk1914
•
3mo ago
unlimited dosing didn't start may 2025. investors discovered it beforehand in a european update. pressure from shareholders convinced the company to PR it.

don't remember when ad infinitum was instituted but maybe someone else does.



Upvote
2

Downvote

Reply

Award

Share

u/YoBee9 avatar
YoBee9
•
3mo ago
There was not a PR, it was just updated on the clinical trials website.


Upvote
3

Downvote

Reply

Award

Share


2 more replies

1 more reply
TTP222
•
3mo ago
Great work and thank you for posting!

I found it interesting that the CEO recently mentioned again that historically BAT is only 8 months. This is a home run and the company already knows it.

The only thing we don’t know is just how many billions they are going to get for GPS and 009. I’m ok waiting a little longer for that answer!



Upvote
11

Downvote

Reply

Award

Share

shaqballs
•
3mo ago
10b minimum, IMO



Upvote
8

Downvote

Reply

Award

Share

TTP222
•
3mo ago
Agree. I think $10b is the floor. Just too much guaranteed revenue with the potential for tens of billions more.



Upvote
6

Downvote

Reply

Award

Share

u/I_Buy_Stock avatar
I_Buy_Stock
•
3mo ago
15b is floor now after the 72 events by end of year. I used to be a 7bil floorer until that pr.


Upvote
9

Downvote

Reply

Award

Share


1 more reply

1 more reply
u/MaestroLiendre avatar
MaestroLiendre
•
3mo ago
We're in a group that we are all in SLS (everyone with their own capacity), and we really think that price will push down hard this week to meet the crazy amount of puts at 3$, but after this the stock could start crawling up again.

Myself I DCA every week a little, so I get at any price.

If for some reason a drop would come, I would actually use the chance to increase my position.

We do really believe that SLS will make a lot of people rich at some point lol.



Upvote
23

Downvote

Reply

Award

Share

Run4theRoses2
•
3mo ago
good luck - your short team is going to need it.


Upvote
9

Downvote

Reply

Award

Share

Impressive_Bluejay71
•
3mo ago
I haven't read this but did you account for those that dropped out, relapsed and discontinued?



Upvote
7

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
3mo ago
•
Edited 3mo ago
Thank you for the comment. Yes, I accounted for this and it is covered in the post above. The model assumes the "Uncured" patients will relapse and die. The bullish signal is that there are simply too many people not doing that.

That was actually one of my main stress tests because I was worried about it too.

For Dropouts/Discontinued (Censoring), I ran a specific "Censoring Bias" check (this is covered within the post above). I forced the model to assume that up to 30% of the patients who dropped out (censored) actually had "bad outcomes" (hidden deaths) immediately after leaving.

The Result from this: It changed the Hazard Ratio by less than 2%. The survival signal is so strong that even assuming the dropouts were failures doesn't kill the thesis.

For Relapsed, the model is built on this. It splits patients into "Cured" (no relapse) and "Uncured" (relapse to death/event)

The "Uncured" group of GPS (about 52-58%) is modeled to relapse and die just like historical patients.

The reason the curve flattens isn't because we ignored relapses. It's because the rate of relapses/deaths has mathematically collapsed to near zero after what has occurred from Dec 2024/Jan 2025 to Dec 26, 2025.



Upvote
13

Downvote

Reply

Award

Share

Run4theRoses2
•
3mo ago
•
Edited 3mo ago
IDMC - guidance to Continue the trial as is - WITH NO MODIFICATIONS - means there are no 'dropouts' etc., sufficient to cause issues w HR...

\ AND for the Life of Me - I don't understand why you don't incorporate ACTUAL PHASE 2 GPS RESULTS?

You can see the OS drops off, after time for GPS Patients.

These are AML Patients who've run the Gauntlet, Heavy Intensive Chemo, Aza+VEN Salvage, who obtain a Second Remission, and are so Unhealthy, they are NOT ELIGIBLE for Transplant. - GPS P3 patient MOS is in the 24- 26 month range --- and 80 Events could occur any day now.

This setting has a 6-8 month Median survival w BAT - according to three dr's who treat actual Phase 3 Patients ---

Comment Image


Upvote
5

Downvote

Reply

Award

Share

u/Just-Finance1426 avatar
Just-Finance1426
•
3mo ago
“You can see the OS drops off, after time for GPS Patients.” 

I’m in agreement with OP on this one, I believe the phase 2 drop off that was observed is not applicable in phase three because the dosing was adjusted to become continual. I think there is a good chance that the drop off is not happening, so we are going to see events come slower and slower.


Upvote
3

Downvote

Reply

Award

Share


1 more reply
neo2551
•
3mo ago
Would you open to share your data and code? I would love to play around.


Upvote
7

Downvote

Reply

Award

Share

u/Trustmebro_analysis avatar
Trustmebro_analysis
•
3mo ago
So $5 leaps then?



Upvote
7

Downvote

Reply

Award

Share

u/I_Buy_Stock avatar
I_Buy_Stock
•
3mo ago
3500 of em here!


Upvote
4

Downvote

Reply

Award

Share


2 more replies
Khataclysme
•
3mo ago
Best I can do right now is 100 shares 😕


Upvote
6

Downvote

Reply

Award

Share

u/shinigamislikapples avatar
shinigamislikapples
•
3mo ago
Oh fuck that's deep 😩


Upvote
6

Downvote

Reply

Award

Share

shaqballs
•
3mo ago
Excellent post! People who naysay will regret it when six months from now this goes up another 1000% or more on a buyout


Upvote
19

Downvote

Reply

Award

Share

u/durtsurfer69 avatar
durtsurfer69
•
3mo ago
Gawdlike DD…thank you for sharing!


Upvote
11

Downvote

Reply

Award

Share

u/TheRock777 avatar
TheRock777
•
3mo ago
I’m not reading this until you post proof that you own 805k shares



Upvote
21

Downvote

Reply

Award

Share

steadyeddy_10
•
3mo ago
He did check


Upvote
5

Downvote

Reply

Award

Share

u/Ateyo94 avatar
Ateyo94
•
3mo ago
Same, sounds very sus. I could make a post tomorrow saying i own 1mil shares etc.



Upvote
6

Downvote

Reply

Award

Share

steadyeddy_10
•
3mo ago
He posted it so


Upvote
9

Downvote

Reply

Award

Share

u/fatdad17924 avatar
fatdad17924
•
3mo ago
How long would a buyout happen after results are released (assuming best case scenario for results)



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
3mo ago
•
Edited 3mo ago
It's hard to predict a timeline, but it is and will be the most sought after oncology acquisition there is. Acquired most likely by relevant strategics like ABBV, BMS, that are already in CR1 and CR2 for AML, etc. as GPS would cause a huge revenue loss for them, and if acquired, a huge gain in revenue as the new standard of care.

My recommendation would be to focus more on the buyout range, posted another comment here going over that in detail.

But as an example, if REGAL FA results come out in Q3 2026, buyout may occur soon after with a closing date in Q4 2026/Q1 2027. My recommendation would be to not even focus on this, and just look at the ranges (the other comment will help a lot here).



Upvote
9

Downvote

Reply

Award

Share

Level_Push467
•
3mo ago
There could be a complex conditional buyout as well with cash and stock. Depends all on who is desperate and has a deal that makes sense to the SLS board and Sterg.


Upvote
3

Downvote

Reply

Award

Share

u/Carbastan24 avatar
Carbastan24
•
3mo ago
Would you say January 2028 LEAPS is a safe enough? Or this has a good chance to drag past that?


Upvote
2

Downvote

Reply

Award

Share


5 more replies
Accurate_Pay_2242
•
3mo ago
Extremely bullish on SLS. Give it a couple months.


Upvote
9

Downvote

Reply

Award

Share

u/Walmartpancake avatar
Walmartpancake
•
3mo ago
Show us your positions



Upvote
14

Downvote

Reply

Award

Share

u/Dry_Competition_7386 avatar
Dry_Competition_7386
•
3mo ago
- I can share my knowledge and experience with you.

- We don't need it. Show us your lambo!


Upvote
6

Downvote

Reply

Award

Share

u/KeyFall3584 avatar
KeyFall3584
•
3mo ago
SHOW US UR BALLS !!!


Upvote
7

Downvote

Reply

Award

Share


1 more reply
u/zeus4270 avatar
zeus4270
•
3mo ago
Amazing DD. Been in SLS for a few years, thru all the dilution etc. for the patients sake, I hope it works as well as you predict. For me, it will mean early retirement.


Upvote
4

Downvote

Reply

Award

Share

Routine-Earer
•
3mo ago
Overall nicely done but too much exaggeration and followed AI too blindly.

The bar graph with the distribution of the '54' survivors in BAT and GPS is one single hallucination. The numbers don't add up to 63 in the GPS arm. It doesn't add up to 54 survivors. A '~' shouldn't be in a bar graph.

This is the only graph I looked at for more than a second and it's seriously flawed and makes me question all other graphs too.

Please do your own graphs using Excel or Graphpad. It's not that hard.

Also what do you respond to the person calling you out on doing a combined 2000 h of research on two stocks over the last year? That seems exaggerated.


Upvote
4

Downvote

Reply

Award

Share

u/Ateyo94 avatar
Ateyo94
•
3mo ago
Show us your 800k position



Upvote
11

Downvote

Reply

Award

Share

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
3mo ago
•
Edited 3mo ago
Respectfully, you guys (this comment and everyone that upvotes comments like this) are all focusing on the wrong things.

I made this post to share DD to help everyone, validate my theses, and get other shareholders' thoughts.

I shared DD that took over a cumulative of 1000+ hours to put together, and there are people that ask ridiculous questions like this that don't even read.

No one is here trying to pump this stock. It will have zero impact on share price and there will be no short squeeze. Most SLS shareholders I've interacted with are very smart people. This is real DD with major upside.

Instead of worrying about what shares other people have, focus on you and your accumulation. Any amount of shares is meaningful. The people that have 5K to 50K shares or around that range is who I'm most excited for. That will be hundreds of thousands to low millions upon buyout. That amount is life-changing as a base in life for people and their families.

Focus on the due diligence, that is what is most important.

Comment Image


Upvote
64

Downvote

Reply

Award

Share

u/Ateyo94 avatar
Ateyo94
•
3mo ago
Fair play…. Let’s hope it works out, I have like 3k shares but might add another 1.5k after seeing that lol


Upvote
9

Downvote

Reply

Award

Share

DawctorMe
•
3mo ago
Respect. You put your money where your mouth is. Excellent DD too


Upvote
9

Downvote

Reply

Award

Share

u/I_Buy_Stock avatar
I_Buy_Stock
•
3mo ago
•
Edited 3mo ago
You need to sell every share and buy '28 leaps bro. I did this but '27 in the summer of '25. Probably shouldn't though because you're sitting all if not just most LTG. But man what a position.


Upvote
2

Downvote

Reply

Award

Share


2 more replies
u/exploringmoon avatar
exploringmoon
•
3mo ago
Big if true.


Upvote
3

Downvote

Reply

Award

Share

u/Bjamnp17 avatar
Bjamnp17
•
3mo ago
I have 100 shares😊


Upvote
3

Downvote

Reply

Award

Share

Technical_Jaguar_348
•
3mo ago
Hi I’m new here and completely illiterate to stock language. Can you dumb this down? Buy SLS (Sellas Life Sciences)? Are we expecting a skyrocket? If so, How much of a skyrocket so I know what a good amount to buy is. Thanks in advance 😊


Upvote
3

Downvote

Reply

Award

Share

u/thenorthernwhiteboy avatar
thenorthernwhiteboy
•
2mo ago
Incredible research man holy crap. Price is up nearly 100% since your post too, do you still see a point in grabbing some shares?



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
Thank you, glad the due diligence is helpful and insightful. And Yes, I am still accumulating and adding every week, with fully diluted share counts of 217MM to 225MM, the upside from $6 a share is 6X to 29X.

For context, GPS annual sales will be at least $4B to $5.5B+ globally and GPS + SLS-009 will be $6.5B to $8.5B.

GPS extends survival to 30-40+ months (as the REGAL data implies), and then there's the cure fraction we are seeing, that the machine learning model predicted is 64%. LTV estimate just based on the long-term survival (and not "cured") is:

​$260K (Y1) + $100K (Y2) + $100K (Y3) + $50K (Y4/Tail) = $510K Total LTV.

$510K ÷ 3.5 years = $145K annual revenue per patient.

The most interesting thing is new transplant ineligible patients in the U.S. (not including globally): There's only about 3,000 new CR2 and 6,000 new CR1 patients each year. (it is more globally)

If everyone mostly died in 8 months (like they do now), revenue would be small ($260K × 9,000 = $2.3B max).

Because GPS keeps patients alive for 3-4 years, by Year 4, you aren't just treating the new patients. You are treating:

2026 survivors (Year 3 of dosing)

2027 survivors (Year 2 of dosing)

2028 new starts (Year 1 of dosing)

This is what creates the 27,000 patient pool and the $4.0B+ annual revenue (and globally will be more, likely $5.5B+ total globally)

4 x 3 to 5 Peak Sales (standard for general acquisitions in Bio) is 20B for example, and this is a breakthrough in oncology (where these types of assets are acquired for 6 to 8 times peak sales).

The floor really is 10B, but I just said 6B because I'm a deep value investor and always assume worst case scenarios. Buyout range is 6B to 40B. Fully diluted share counts is 217MM to 225MM, so 10B would be about $46.40 a share.

The range is that broad for buyout because we ultimately don't know what the bidding war between strategics like ABBV, BMS, etc. will lead to, as we're just talking about GPS here for AML CR2 and CR1. We haven't even discussed SLS-009 (which will be bigger than GPS) for the Frontline, which is in Phase 2B, we haven't talked about the other indications from the WT1 targeting that is present in 20+ cancers, etc.



Upvote
3

Downvote

Reply

Award

Share

u/thenorthernwhiteboy avatar
thenorthernwhiteboy
•
2mo ago
Is there any risk that the company has to continue to dilute to the point that shares are worth next to nothing and at that point a larger company would come and buy the technology?



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
As of Jan 2026, they have $98M of cash on their balance sheet, and total quarterly spend is about $7M. They have plenty of runway. The REGAL trial is at 72 out of 80 events as of Dec 26, 2025.

And as of today actually, they have $115M in cash on their balance sheet, as $16.1M of the outstanding warrants were exercised. So, $115M in cash with a per quarter burn rate of about $7M.

There is no risk of dilution before REGAL final analysis readout, other than what we already know and factored in already, of the outstanding warrants, which as of today, are about 31.5MM.

Fully diluted share count will be 217MM to 225MM, so 10B for example, would be about $46.40 a share.


Upvote
4

Downvote

Reply

Award

Share

u/jayantoine647 avatar
jayantoine647
•
2mo ago
Is it still worth to get in? What’s the PT?



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
Yes, I am still accumulating and adding every week, with fully diluted share counts of 217MM to 225MM, the upside from $6 a share is 6X to 29X.

For context, GPS annual sales will be at least $4B to $5.5B+ globally and GPS + SLS-009 will be $6.5B to $8.5B.

GPS extends survival to 30-40+ months (as the REGAL data implies), and then there's the cure fraction we are seeing, that the machine learning model predicted is 64%. LTV estimate just based on the long-term survival (and not "cured") is:

​$260K (Y1) + $100K (Y2) + $100K (Y3) + $50K (Y4/Tail) = $510K Total LTV.

$510K ÷ 3.5 years = $145K annual revenue per patient.

The most interesting thing is new transplant ineligible patients in the U.S. (not including globally): There's only about 3,000 new CR2 and 6,000 new CR1 patients each year. (it is more globally)

If everyone mostly died in 8 months (like they do now), revenue would be small ($260K × 9,000 = $2.3B max).

Because GPS keeps patients alive for 3-4 years, by Year 4, you aren't just treating the new patients. You are treating:

2026 survivors (Year 3 of dosing)

2027 survivors (Year 2 of dosing)

2028 new starts (Year 1 of dosing)

This is what creates the 27,000 patient pool and the $4.0B+ annual revenue (and globally will be more, likely $5.5B+ total globally)

4 x 3 to 5 Peak Sales (standard for general acquisitions in Bio) is 20B for example, and this is a breakthrough in oncology (where these types of assets are acquired for 6 to 8 times peak sales).

The floor really is 10B, but I just said 6B because I'm a deep value investor and always assume worst case scenarios. Buyout range is 6B to 40B. Fully diluted share counts is 217MM to 225MM, so 10B would be about $46.40 a share.

The range is that broad for buyout because we ultimately don't know what the bidding war between strategics like ABBV, BMS, etc. will lead to, as we're just talking about GPS here for AML CR2 and CR1. We haven't even discussed SLS-009 (which will be bigger than GPS) for the Frontline, which is in Phase 2B, we haven't talked about the other indications from the WT1 targeting that is present in 20+ cancers, etc.


Upvote
3

Downvote

Reply

Award

Share

steadyeddy_10
•
3mo ago
🔥


Upvote
5

Downvote

Reply

Award

Share

Run4theRoses2
•
3mo ago
•
Edited 3mo ago
Expecting the Instutions to start Loading Hard - should see a Double in the Share Price in the next days, the Positive P3 Result is worth 70x the current manipulated market value.

you state the historical BAT MOS is 10 months ... prove it. ???

All Actual data confirm BAT MOS is 6-8 months.

Historical (*pre VEN) MOS is just 5/6 months - with Aza+ven it is 6-8 months.

Comment Image

Upvote
5

Downvote

Reply

Award

Share


1 more reply
u/WhoCares450 avatar
WhoCares450
•
3mo ago
I think we will land 10-12/share. That's a baseline, not a bullish case. But that's how I like to operate to be safe. That assumes 4x% lapse for patients albeit a bit less optimistic than OP, which I apply to avg cases annually in US, i.e. buying market. Bullish take can take this to $15/share. It will also depend on financial structure, if it's CVR based, which is very likely.



Upvote
2

Downvote

Reply

Award

Share

u/TaoTeCha avatar
TaoTeCha
•
3mo ago
That's only a $2.5 Billion buyout. If the drug is successful I think it will be much higher than that.



Upvote
4

Downvote

Reply

Award

Share

u/WhoCares450 avatar
WhoCares450
•
3mo ago
Like I said, I operate on a side of caution. In a bullish scenario it can get closer to $4B. I'm happy selling at $12/share.



Upvote
2

Downvote

Reply

Award

Share

u/Murxxxismus avatar
Murxxxismus
•
3mo ago
Onureg for example was bought for 4.4 billion inflation adjusted. It was 2.9 bil in 2008. 4,4 bil for SLS would 20,24 dollar share price. I think the floor is higher than that with the data we are gonna be looking at. 7 billion would be around 32 dollar share price. That's the minimum from my perspective.


Upvote
4

Downvote

Reply

Award

Share

u/Glass_Crazy_3996 avatar
Glass_Crazy_3996
•
3mo ago
A 42–48% cure-fraction tail needs the majority of patients (50+) followed 5+ years with near-zero late events; REGAL’s event-driven end before that, prioritizing HR detection over plateau confirmation.


Upvote
2

Downvote

Reply

Award

Share

u/pkinla avatar
pkinla
•
3mo ago
If the trial never hits 80, sls would trigger fa; what are chances of 1 and if so what will trigger sls to do the fa?



Upvote
2

Downvote

Reply

Award

Share

artynonymous
•
3mo ago
So, we talking immortality now?


Upvote
5

Downvote

Reply

Award

Share


1 more reply
u/Such-Leg4898 avatar
Such-Leg4898
•
3mo ago
Thank you very much for your work.  A DD masterpiece.   I have to admit that I do not understand all of it but about half of it I do. Gives me a very good feeling about my position and my financial future. Again thank you for your time spent on this for the benefit of all of us.  🙏👍


Upvote
2

Downvote

Reply

Award

Share

Run4theRoses2
•
3mo ago
U/just-finance1426 all patients have been in trial nearly 24 months at a minimum. Even with a median of 30 months for GPS, we would have nearly 50% of the GPS arm, 30 patients give or take, who will have died and we know that nearly all of the control arm patients have died, plus or -60 think about it?


Upvote
2

Downvote

Reply

Award

Share

mad_papooser
•
3mo ago
I don't disagree with most of your results. My modeling has revealed almost the exact same parameters, so I feel more confident about it now seeing someone else mirror what I have found. Just a few things I can quibble with: You said: "72 of 80 required events have occurred as of Dec 26th, 2025. Thus, 54 patients are still alive at month 58". You can't make that assumption because patients have definitely been lost to censorship. Historically, 15-20% is a fair number for the BAT arm and 5% for the GPS arm (less patients likely to leave if seeing benefit. That would be roughly 25 patients overall lost to censorship, which means that potentially on 30 or so are still alive and in the trail. This also helps explain some of the slowdown as well, because you have GPS long-responders, and likely some BAT long responders, so your pool of "easy" deaths is depleted.Second, your model doesn't accurately reflect the HR in the first 4 months or so of the trial.

Lastly, you are assuming patients who leave the trial (censored) are random. It's almost certain that more BAT patients are leaving the trial than GPS. Your modeling doesn't account for this- censored, vs "dead". It artificially inflates the BAT survival curve in the Kaplan-Meier analysis.

Comment Image


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
3mo ago
First off, thank you for your comment, appreciate it.

In regards to this: "You said: "72 of 80 required events have occurred as of Dec 26th, 2025. Thus, 54 patients are still alive at month 58". You can't make that assumption because patients have definitely been lost to censorship."

So, I did do the censoring stress-test with the model. This is covered within the post above towards the end. In Phase 2 for GPS, for AML CR2 (not eligible for transplant), this was number was 15%. So, I stress tested all the way up to 30%. The cure fraction barely moved and HR only changed by 2% from this stress test.

The likely/realistic makeup of those censored is likely the majority being the BAT arm (for example, 70%) like you said and the rest being the GPS arm (30%), like you said.

When I reran the censoring stress-tests under this proportion, like you said, results improved across the board for GPS.

But I didn't want to assume this. I wanted to stress-test under worst case scenarios.

Like for example, I even stress-tested if all the 30% censoring was just GPS, not any BAT, and at 30%, every single dropout being a GPS patient who secretly died. Which is absurd, but when I tested this, at a BAT mOS of 10 to 13 months, this crazy absurd scenario gave a Cox HR of 0.249-0.432 with P(success) 95%-100%. Stratified HR would of course be higher, but still, success in this stress test.

As a deep-value investor, I look at more of what the worse case scenarios would and under that, would the thesis still hold.

Like you said, if a patient disappeared instead of dying on the record, the Control arm's survival curve stays high. It looks "artificially inflated" (aka fake better).

You also said this: "This also helps explain some of the slowdown as well, because you have GPS long-responders, and likely some BAT long responders, so your pool of "easy" deaths is depleted."

On pool depletion, yes you're absolutely right, and that's exactly what the cure-fraction model captures. The "easy deaths: (non-responders, short-surviving BAT patients) deplete early. What's left is the plateau population. We're in complete agreement here.

You said this as well: "Second, your model doesn't accurately reflect the HR in the first 4 months or so of the trial."

On the early HR, you're right in that vaccine trials typically show delayed separation in the first 3-6 months, and the model doesn't explicitly handle that. But we're fitting cumulative events at months 46 and 58, which are dominated by the long term behavior. If anything, modeling the delayed effect properly would require an even higher late-stage cure fraction to compensate.

Appreciate your comment, this is exactly the type of the thoughts/discussion I wanted to get to help validate my theses. Hope anyone reading these gets a ton of value.


Upvote
7

Downvote

Reply

Award

Share

RyanBloods716
•
2mo ago
Are you worried about the companies dilution? They are seeking additional financial investment and explicitly stated they are raising capital and it may be dilutive in the 10k report.
That's one factor that worries me before sinking some cash into this, Overall your due diligence was so good it inspired me to do my own and I liquidated one of my smaller portfolios and bought some shares.
What do you personally believe about the companies fundraising and possible dilution and how do you value SLS in light of that?



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
Thank you for your comment and awesome. Replied to another comment asking a similar question yesterday, so I'll share that here. Dilution is a threat when a trial has 3 years left (that is the furthest from the case here). The REGAL trial is at 72 out of 80 events as of Dec 26, 2025. As of Jan 2026, they had $98M of cash on their balance sheet, and total quarterly spend is about $7M

Big picture, the warrants isn't anything to worry about. The entire thesis and upside from REGAL Final Analysis readout and buyout is based on the fully diluted share counts, including warrants.

Fully diluted share count is 217MM to 225M, and the outstanding warrants overhang is still 40M now.

But just some facts on this, and as confirmed by Anson's very recent amended 13G/A SEC filing on February 17, 2026, their warrants contain a strict Beneficial Ownership Limitation. They are legally blocked from exercising any warrants that would push their total ownership above 4.99% of the outstanding shares.

Because they are currently hovering right at that 4.9% line, they are forced into a bottleneck.


Upvote
4

Downvote

Reply

Award

Share

Ambitious-Map5299
•
2mo ago
thanks


Upvote
2

Downvote

Reply

Award

Share

u/Due-Papaya-6217 avatar
Due-Papaya-6217
•
3mo ago
Hmmmmm……


Upvote
4

Downvote

Reply

Award

Share

daskott
•
3mo ago
mucho text

all in


Upvote
3

Downvote

Reply

Award

Share

Wolvshammy
•
3mo ago
I'm gonna say this post is HIGHLY suspicious. You did 1000 hours of research on this stock? You a full time trader or do you have another job? If the former, you have time to trade stocks and do 6 months of 40 hours per week of research? If another job, you have 6 months of time at 40 hours a week to do this research? I find that incredibly hard to believe. What's harder to believe is that you ALSO did exactly 1000 hours of research on CNC stock 10 days ago? One full year of research on 2 stocks. And you only have 2 total posts on your account? Sus af. I have done more research on ELTP that anyone alive that I know (there are also a few other very talented investors who do great research as well and provide great info). I've researched ELTP since 2017 and didn't invest in is until 2021 and yeah I probably have 1000 hours of research....over a NINE year period. My account is also flooded with original DD posts on ELTP and response posts.

I'm not saying whether this is a good stock or not, because I haven't researched it, but I'm already suspicious of the quality of the DD if I spot a likely lie like that in the first paragraph.



Upvote
4

Downvote

Reply

Award

Share

Level_Push467
•
3mo ago
Counting hrs, mate? Not the quality of what he put out? When you own 800K shares, you do your DD. Never heard of you either.


Upvote
7

Downvote

Reply

Award

Share


3 more replies
u/Interesting-Play-489 avatar
Interesting-Play-489
•
3mo ago
I hope OP responds to you as I’m curious as well.

Though, as someone noted below on a similar comment, is that all you really have to say about this post?

I’ve seen a lot of your DD on ELTP and I’d be curious to read your genuine take on SLS.


Upvote
3

Downvote

Reply

Award

Share


1 more reply
u/ThundarTom53 avatar
ThundarTom53
•
3mo ago
Great work, and I realize that the curves represent observed real world numbers, so I understand some of what I am about to ask is already figured in, but what about good old run of the mill death? These are unhealthy individuals who have been through nasty treatments for an even nastier disease. GPS may keep the disease dormant, but it can't reverse the damage that has already been done. I'm not saying that the HR will approach the primary target, but as time goes on these people will die (and at an accelerated rate to "healthy" people). Would this change your predictions if considered?



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
3mo ago
•
Edited 3mo ago
Thank you for your comment. Remember this in AML CR2 (not eligible for transplant), and that both arms had the nasty treatments (chemo induction). If background frailty was the main killer, the control arm (BAT) survivors would be dying at the same rate. Instead, we see a massive divergence (about 71% alive on GPS vs. 10% on BAT). That gap can't be explained by general health, it can only be explained by the drug stopping the cancer.

In REGAL, it doesn't matter if a patient dies from AML relapse, a heart attack, or frailty from past chemo. They all count as events. The 72 events we have observed so far already include those background deaths.

If these patients were dying at an accelerated rate due to being "unhealthy," we would see it in the recent data. Instead, we saw only 12 deaths from Dec 2024/Jan 2025 to Dec 26th, 2025 across the whole study. That is a remarkably low death rate of about 1 per month. It proves that frailty isn't driving a mass die off.

While these patients have been through nasty treatments, the risk of dying from AML relapse (which historically before GPS, kills 90% of patients within 2 years) is vastly higher than the risk of dying from run of the mill causes (maybe 3-5% per year).

The "cure fraction" in the model is that transition point. The curve flattens out exactly when patients "stop dying" of AML (meaning stability) and return to the "normal" (realistically slightly elevated) mortality risk of their age group. The model doesn't predict immortality, it just predicts they "won't die" of leukemia.


Upvote
6

Downvote

Reply

Award

Share


1 more reply
u/Murky-Ambition3898 avatar
Murky-Ambition3898
•
3mo ago
Is the stock going to go up or go down, and by how much? LOL.


Upvote
2

Downvote

Reply

Award

Share


1 more reply
u/hariharsharma avatar
hariharsharma
•
3mo ago
Novice here. Don't understand the details but they are thorough, not less than a scientific journal article. Thanks. I only want to know, where SLS will be immediately after results.


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
Will it work the same way for Ovarian cancer as well? As it's an antigen vaccine and don't need to go into the cell but perforate cell membrane of the cancer cells and destroy it. So works the same way for any cancer that express WT1??



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
Thank you for your comment. It's great to see you discussing the big picture with WT1 being expressed in almost 20+ cancers. WT1 is a universal target, which is why this drug has so much potential. But one small correction on the cellular mechanics of how it destroys the cell.

The vaccine itself does not perforate the cancer cell. GPS is an immunotherapy. It's like a wanted poster where the immune system of the patient will recognize who to look that has WT1 expressed. When injected, it trains the patient's own immune system (specifically CD8+ Cytotoxic T-cells) to recognize the WT1 protein. Once trained, those T-cells are the ones that hunt down the cancer, lock onto the membrane, and release a protein called perforin to punch holes in the cancer cell and destroy it.

But to answer your core questions:

Does it work the same way for Ovarian cancer? Yes, WT1 is expressed in over 85% of ovarian cancers. SELLAS has actually already run Phase 1/2 trials in advanced ovarian cancer combining GPS with Keytruda/Opdivo. It successfully triggered that exact T-cell response and pushed median Overall Survival past 18 months in a very difficult to treat population.

Does it work for any cancer expressing WT1? Exactly. Because the trained T-cells only look for the WT1 antigen, they don't care if the tumor is in the blood (AML), the lungs (Mesothelioma), or the ovaries. This is exactly why the National Cancer Institute ranked WT1 as the number 1 priority target for immunotherapy in the world."

They specifically focused on AML and dominating AML with SLS-009 + GPS. Outside the lives saved and benefits for patients, strategic acquirers get excited about that given if they acquired SLS, that revenue stream would be protected for at least 7 years without any competition, the acquirer would have a monopoly in AML CR2 (not eligible for transplant), total dominance in CR1, and tons of penetration in the frontline with SLS-009. Strategic acquirers already in AML include ABBV, BMS, etc.


Upvote
1

Downvote

Reply

Award

Share


2 more replies
u/Prestigious_Bad1855 avatar
Prestigious_Bad1855
•
2mo ago
Can anyone guess why there are 20% non responders in GPS arm? As we can see almost all AML patients exhibit WT1 over expression.


Upvote
1

Downvote

Reply

Award

Share

u/srgtchuckles avatar
srgtchuckles
•
1mo ago
Hey! Sorry if this is a stupid question, I'm a teenager and this is one of the first companies I've invested in for biotech. I understand this wouldn't be a simple exponential model, but how does it prove a cure-fraction model just because events/month are decelerating? Couldn't there be other reasons for this deceleration?



Upvote
1

Downvote

Reply

Award

Share

95

u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
1mo ago
•
Edited 1mo ago
Hey, not a stupid question at all. So, the ML models I built are not "guessing" the split, they are mathematically deriving it from two immutable, SEC filed facts, 60 total events at month 46, and 72 total events at month 58.

We know the total number of deaths, and the ML models tested for every BAT mOS from 8 to 23, and the biological/clinical cap in AML CR2 (not eligible for transplant) is 6 to 12 months.

AML CR2 (not eligible for transplant) does not have a long tail. It is a relentlessly aggressive disease.

In a standard parametric survival distribution without a cure fraction (like a Weibull), the hazard rate for a cohort of 54 elderly, heavily pretreated AML patients does not spontaneously cut itself in half. The only way the math works is if a large portion of those 54 survivors are experiencing a hazard rate of near zero, which is the exact mathematical definition of a cure fraction.

The deceleration pattern, peaking at 14.1 events per 6 months during months 31-36, then dropping to 8.8 (months 43-48), then 6.2 (months 49-54), then 4.4 (months 55-60), this is a sustained, monotonic decline over 24+ months. That is not a random fluctuation. An exponential model produces a gentle decline (fewer patients remain at risk), but the cure-fraction model matches the shape of the decline, not just the endpoint.

Furthermore, if you fit a Weibull, Log-Normal, Gamma Frailty, or Piecewise hazard to the same constraints (no cure assumption), they all overshoot. I tested 6 model families. Every single one that matches 60 events at month 46 and 72 at month 58 has an internal structure that includes either an explicit cure fraction or an implicit one (a sufficiently heavy tail in Weibull/Log-Normal that mimics cured patients). The math forces you there regardless of model choice.

REGAL is successful up to a BAT mOS of 20 and the biological cap in this patient population, AML CR2 (not eligible for transplant) is 6 to 12 mOS.

The 99.99% statistical probability of success for REGAL success is real and genuine.

Also, just wanted to add that it's fantastic that you're a teenager and are reading this due diligence. The fact that you have these questions is great. And this is also the first biotech I've ever owned as well. I've been a deep value investors for years and this is the most asymmetric opportunity with a gigantic margin of safety that I have ever come across in my life.

Comment Image

Upvote
3

Downvote

Reply

Award

Share


1 more reply
u/WhoCares450 avatar
WhoCares450
•
3mo ago
A lot of good info. I have SLS as well, although not near OP. One flaw, revenue per patient is garbage, hence your valuation is garbage. Why? Because at that cost there will not be enough sales. They will make it more reasonable, likely around 50-60/year. So decrease your valuation 2.5x.



Upvote
-2

Downvote

Reply

Award

Share

Prestigious-Duck-189
•
3mo ago
Expected revenue per patient is mentioned in the Sellas investor decks. Fyi


Upvote
6

Downvote

Reply

Award

Share


8 more replies
u/Confident-Web-7118 avatar
Confident-Web-7118
OP
•
3mo ago
Replying here so people don't get confused. First off, thank you for your comment, appreciate it. The peak revenue estimates I shared are correct. I think you're forgetting a few things:

First is about Onureg (oral azacitidine), which is BMS' drug. GPS had 1.5X the results of Onureg during Phase 2 in CR1, and this was before the unlimited dosing or even just increased dosing that occured later on in Phase 3 (right now).

​Price: Onureg is priced at roughly $24,000 - $28,000 per month (approx. $300,000+ per year).

​Second is tha insurance companies already pay about $300k/year for a drug (Onureg) that offers a 24-month median survival in CR1 (8 to 10 in CR2, if that). GPS offers 30+ months of survival in CR2, way above that in CR1, insurance cannot force a price of $50k. It would be priced at least at parity with the inferior standard of care.

​And third is orphan drug pricing power. GPS has Orphan Drug Designation. The median cost for orphan cancer drugs often exceeds $200,000 annually. A price tag of $50k/year would be suicidally low for a life-extending biologic in a fatal disease.


Upvote
7

Downvote

Reply

Award

Share


2 more replies
u/ProfessionalDesk1914 avatar
ProfessionalDesk1914
•
3mo ago
do you know how much ven/aza is per patient? it's over $450k a year


Upvote
3

Downvote

Reply

Award

Share


1 more reply
Level_Push467
•
3mo ago
There is no award for Dumb, is there?


Upvote
1

Downvote

Reply

Award

Share


2 more replies
all-cap-be
•
3mo ago
Ai gave me like 5 red flags for the post, first one:

My Critical Red Flag Analysis 🚩 🚩 RED FLAG #1: Wildly Optimistic Projections Claim: GPS median OS = 97-183 months (8-15 years)[reddit] Reality check: • Historical AML CR2 patients: 8-11 months median OS • Even successful AML maintenance therapies extend this to 15-24 months • No AML therapy has ever achieved 8-15 year median OS in this population • This would be the greatest oncology breakthrough in decades • If true, GPS would be worth $50B+, not $500M market cap My assessment: This is fantasy-level projection that ignores oncology reality.



Upvote
-4

Downvote

Reply

Award

Share

Prestigious-Duck-189
•
3mo ago
Garbage in garbage out.


Upvote
1

Downvote

Reply

Award

Share

u/The_Hustler_Guy avatar
The_Hustler_Guy
•
3mo ago
The pumpers are insane and don't live in reality.


Upvote
0

Downvote

Reply

Award

Share


2 more replies
AdSeparate6751
•
3mo ago
That was a lot. Your post would greatly benefit from a summary paragraph or an abstract like from research articles.



Upvote
-1

Downvote

Reply

Award

Share

shaqballs
•
3mo ago
You should maybe just read the little pump and dump posts instead of this one because this is what actual dd is. It’s new to this sub lol


Upvote
11

Downvote

Reply

Award

Share

mad_papooser
•
3mo ago
•
Edited 3mo ago
duplicate


Upvote
0

Downvote

Reply

Award

Share


Guilty_Ad_8433
•
3mo ago

firewire1212
•
3mo ago
