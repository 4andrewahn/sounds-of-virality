# Sounds of Virality 

---
### About the project 
Nowadays, TikTok has become an essential platform for the music industry. The virality of its short-form content has opened up new avenues for music to reach new audiences, but what exactly is it about the types of music that go viral? Is there a grain of truth when people say something "sounds like a TikTok song"? These are the questions this project hopes to answer. 

In this exploration of sounds, there will be 3 phases:
1. Data Collection
2. Data Analysis 
3. Data Visualization 

--- 
### Phase 1: Data Collection
This project will use Spotify's API to gather information about songs and their 12 associated audio-features as provided by Spotify. The songs analyzed will be split into 3 groups by their genre: Pop, Hip-Hop, and Viral. The specific songs to be included in our dataset will be determined by playlists that fit two criteria: the playlist must be curated by Spotify (instead of a user), and the playlist must have atleast 1 million likes. By sampling songs with this method, we hope to gain a broad-level overview of popular songs from each genre for a fair and accurate comparison. 

> The full data collection process can be viewed in `data_collection.ipynb`

The final compiled dataset will be contain the following attributes:
| **Attribute** | **Data Type** | **Description** |
| -------- | ------- | ------- |
| id | string | The unique Spotify ID for each track|
| acousticness | float | A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic. |
| danceability | float | Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable. |
| energy | float | Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy. |
| instrumentalness | float | Predicts whether a track contains no vocals. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0. |
| key | int | The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1. | 
| liveness | float | Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live. |
| loudness | float | The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Values typically range between -60 and 0 db. |
| mode | int | Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0. |
| speechiness | float | Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks. |
| tempo | float | The overall estimated tempo of a track in beats per minute (BPM). |
| time_signature | int | An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4". |
| valence | float | A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry). |
| name | string | The name of the track. |
| artist | string | The primary artist of a track. |
| genre | int | The encoded genre group of a track. |

---
### Phase 2: Data Analysis 
Using the dataset compiled from the data collection phase, the data analysis phase aims to isolate the audio-feature characteristics that are most distinctive for each genre. We will use the analysis completed here to guide our visualizations for the next phase. 

> In progress... 

---
### Phase 3: Data Visualization 
> In progress...