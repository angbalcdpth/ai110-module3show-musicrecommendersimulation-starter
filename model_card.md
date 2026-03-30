# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

### Experiment finding (added):

The current logic can create a “filter bubble” for high-energy users because a very strong energy weight pushes the same energetic songs to the top for many profiles, even when genre and mood are different. In particular, the adversarial profile (sad jazz with target_energy=0.9) still returns high-energy danceable tracks. This illustrates that the model can ignore mood and genre if numeric similarity wins, so certain user goals (e.g., “sad, mellow” listeners) may be poorly served. 

Another bias is the small dataset itself (and potential genre imbalance), which can make the model overly dependent on a few popular songs being surface again and again; this is especially visible when the same song appears near the top in multiple profiles.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

### Experiment summary (added):

I tested four profiles: high-energy pop, chill lofi, deep intense rock, and an adversarial profile (sad jazz with very high target energy and tempo). 

What surprised me was that `Gym Hero` kept appearing at or near the top even for the adversarial profile. In simple terms, the system learned that it likes songs that match the energy level more than it cares about whether the mood and genre are right. For someone asking for “happy pop,” the model still sees a song like `Gym Hero` as very good because the energy and tempo are close, and it has a popularity bonus, so the score is high. This explains why the same song can pop up for different user tastes.

Another surprise was: when I doubled energy weight and halved genre weight, the effect was strong and the high-energy songs dominated even further, which is evidence the scoring formula is the main driver, not the underlying song labels.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

### Reflection (added):

My biggest learning moment was discovering how the weight values in a simple score formula can completely change what the system thinks is a good recommendation. A 2x energy weight and 0.5x genre weight change made the entire output feel like a different model, and that was a strong reminder that these systems are often “just math” under the hood.

Using AI tools and Copilot through the workflow helped speed up scaffold and debug steps, especially when building the test harness and wording evaluation feedback. I still double-checked output logic and wording in the code (especially in `score_song`) by running local tests, because the AI suggestions are good but can miss subtle intended behavior and exact variable semantics.

I was surprised by how correctly simple algorithms can still feel like recommendations: once you combine genre, mood, and scalar similarity, top results look like a personal playlist even though there is no machine learning model, just hand-tuned weights.  

If I extended this: I would add a genre/mood penalty term, normalize each feature to 0-1 and create tunable user-specific weights, and include a diversity metric so the top suggestions aren’t always the same set of songs.

---  
