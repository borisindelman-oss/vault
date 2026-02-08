Boris Indelman  [7:40 PM]  

Hey Zak  
  
I want to implement interleaving for our model. I've looked in your branch and saw that you use `interleave_control` ?  
But when I asked Naman he said it's not working with torchscript.  
Are you converting to trt?

Zak Murez  [8:06 PM]  

Currently I am using the legacy torchscript interleaving. See [here](https://github.com/wayveai/WayveCode/blob/zmurez/pudo/wayve/ai/experimental/compile_with_baseline.py). Later we can switch to robot interleaving once that settles. Note that I don't currently output interleave outputs so we don't log which model is in control but this can be added if you want.

  

Boris Indelman  [8:08 PM]  

thanks I didn't see that. That's what I was expecting to see.  
how would you log that? I've been using prints but I rather see it in foxglove  
  
downside for me is that each combination of baseline and pudo model would need licensing ![:aaahh:](https://emoji.slack-edge.com/T6A5E9XGT/aaahh/572e5508d11ae33a.png)

  

[8:09 PM]

also how do you calculate 100 m from pin? green pixels count?

  

Zak Murez  [8:25 PM]  

Green pixel count (not actually calibrated to meters I just said that to make it easy)

  

Boris Indelman  [8:27 PM]  

yes I figured

  

Zak Murez  [8:28 PM]  

See [https://github.com/wayveai/WayveCode/blob/main/wayve/ai/scripts/interleaved/compile.py](https://github.com/wayveai/WayveCode/blob/main/wayve/ai/scripts/interleaved/compile.py)  
[https://github.com/wayveai/WayveCode/blob/main/wayve/ai/zoo/deployment/interleaved_wrapper.py#L20](https://github.com/wayveai/WayveCode/blob/main/wayve/ai/zoo/deployment/interleaved_wrapper.py#L20)  
  
If you ingest your model by itself then interleave with this script then it will be logged in the mcaps and be ingested throughout (including showing on the console).

  

[8:29 PM]

Licensing we always need to do 1 licensing route per new model. I don't see why this leads to more licensing routes?

  

[8:29 PM]

So make your own interleave script but make sure the nicknames match the standard and then output these 2 signals

  

Boris Indelman  [8:31 PM]  

I meant that if the interleaving was in the InterleavedModelRunner then there is no need for another licensing. We just specify in the experiment which 2 models to interleave

  

Zak Murez  [8:35 PM]  

Oh, you mean for A/B comparison of 2 models? Or fix mixing baseline with a pudo model?

  

[8:38 PM]

Regardless, I always just test the mix and never test the individual model. So no need for extra licnesing. Later if the model is good and we want to run it by itself we need to do an extra licensing route. Although here I use driving assertiveness as a hard switch. eco is only model 1, bold is only model 2, normal is the mix

  

Zak Murez  [8:47 PM]  

Do you have 15mins to chat now? Got a question for you but a meeting in 15mins

  

Boris Indelman  [8:48 PM]  

not right now. I'll try to catch you later today ![:pray::skin-tone-3:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-medium/1f64f-1f3fc@2x.png)

  

Zak Murez  [8:48 PM]  

Sounds good.

  

Boris Indelman  [8:45 AM]  

Hey Zak  
  
How does temporal caching works in your interleaving imp? Do you assume that it's ok when switching to use the previous model caching?

  

Zak Murez  [8:48 AM]  

You get cache misses following the swap. Models are trained with temporal dropout to make them robust to this. But that doesn't fully resolve it so we continue to send the last waypoint plan (repeat the last valid one) for the first few forward passes. See [https://github.com/wayveai/WayveCode/blob/main/wayve/ai/zoo/deployment/interleaved_wrapper.py#L98](https://github.com/wayveai/WayveCode/blob/main/wayve/ai/zoo/deployment/interleaved_wrapper.py#L98)





Tom Boehling  [11:31 AM]  

replied to a thread:

Hi everyone, the mapped Uber data looks really promising! With the filters I have in place now, I only saw relevant data so far.  
  
I’ve mapped the Uber PUDO data to our all_data table.  Each PUDO event is matched to the longest standstill segment within a 10-second window.  I’ve created a new table containing three timestamps: the Uber timestamp, the start of standstill, and the end of standstill.  
  
Notes:  

- For pre-training one could easily filter for standstill_start - 15s and standstill_end + 15 (should roughly give the whole PUDO event).
    - [@boris](https://wayve-ai.slack.com/team/U09RQU5V68M), [@tapan.mujumdar](https://wayve-ai.slack.com/team/U09NSLK1Q82), [@alon.davidi](https://wayve-ai.slack.com/team/U09NW7EHKD2) What do you need for training? Is the table enough, or do you have another table schema in mind? I can change it depending on your needs.
- I included a few columns for training data selection: pickup/dropoff, road_class, very big geo index, night/day, weather, gear_reversed, acceleration, curvature_change)
- Important: timestamps are in seconds not us (so multiply by 1_000_000)

  
  
Statistics and Visualisations: [Databricks](https://adb-7835963732836817.17.azuredatabricks.net/editor/notebooks/246569510427994?o=7835963732836817#command/5825235315928253)  
  
A few stats:  

- total data from uber: 344,474 trips -> **688,948** **PUDOs**
- standstill segments **based on gear**: **124,688 PUDO matches**
    - bad matching outcome - no further investigation
- standstill segments **based on speed==0**: **457,174 PUDO matches**
    - only complete data (excluding beginning/end of runs): 415,138 PUDO matches
        - **only valid data (excluding wrong uber trip data): 407,030 PUDO matches**
    - Either gear status is not always correct or Uber drivers often only hit the brakes for PUDO
-  [@Malik](https://wayve-ai.slack.com/team/U036H2VAXRD) unrelated to PUDO, we could also do some trip based analysis, like how long trips usually are, ... (I don't know if there is a need)

  
  
Extended visualisation:  

- I only wanted to add a plot with speed/gear for validation, but Codex decided to also make it look better ![:smile:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-medium/1f604@2x.png)
- I synced the timestamps with the video
- See new visualisation below + explanation of timeseries speed/gear plot




**FYI – Urban PUDO testing update**  
There is now a **dedicated temporary Urban-Only PUDO route** (L1→~~L1~~,L2 Alpha-1 derived, Market Road start/end).  
**Controls are mandatory:**  
 • **Model:** must be tagged _Urban-PUDO-Only_ and _Not-For-Highway_, with clear notes on the model timeline  
 • **Experiment:** description must clearly and obviously state _PUDO urban testing only – no highway use_  
 • **Licence** **Route:** restricted to urban only  
[PUDO Temp Urban Licence (expires 01/04/2026) – Start at Market Road](https://console.sso.wayve.ai/route/00bdc0dc-6d04-4df2-a917-adae96ef9176)  
Models approved under this process **can only be used for PUDO testing**, are **urban-restricted**, **time-limited**, and will be reviewed before the end of Q1.  
**VSOs are still expected to flag any unsafe or dangerous behaviour observed during these temporary licensing runs**, as per normal processes.  
**Shift Leads need to be aware of these restrictions** when planning and assigning runs.  
Please reach out if there are any questions and read attached safety justification (edited)



FYI there have been a few updates to the PUDO SOP document regarding where/what a good PUDO stop is in the US. Specifically, we've edited a couple of situations/spots where we DO stop, and where we DON"T stop:  
  

- **Never stop:**
    - Alongside curbs with "**No Stopping**" signs, whether there's a red curb or not
- **Allowed to stop:**
    - Alongside curbs with "**No Parking**" signs, even if there's a red curb

  
  
Also, we were initially running PUDO missions and choosing PUDO stop locations with the assumption that the passenger would be waiting there and would just hop in. However, after some consideration, we've decided that it's more likely that we might have to wait a couple minutes for the passenger to come out and get in the vehicle, and we should be choosing PUDO stop locations based on that. If you don't feel comfortable stopping in location for two minutes (double parking on a narrow road, stopping in a red zone, stopping behind parked cars in a parking lot, etc), then choose a new place to stop.  
  
Please read the SOP document for more details, and keep in mind that it still may change as we continue testing this feature. And special thanks to [@Victor](https://wayve-ai.slack.com/team/U09E5JQC0ES) for helping me hash these new points out!  
  
[https://docs.google.com/document/d/19_supcKMuus13WO_Ub9s3s-cLXWIpE74Rdv6gveTbBM/edit?usp=sharing](https://docs.google.com/document/d/19_supcKMuus13WO_Ub9s3s-cLXWIpE74Rdv6gveTbBM/edit?usp=sharing)