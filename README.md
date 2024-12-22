# Expert-system-to-recommend-soccer-players
Midterm project assignment for introductory artificial intelligence course


![Screenshot 2024-12-23 010622](https://github.com/user-attachments/assets/6b1c1be6-2b7a-4673-872e-380a0a03f45c)


1. Introduction

   - System goal: Build an expert system capable of suggesting soccer players based on the characteristics the user desires.

   - System benefits:

      + Support users to find players that match their requirements quickly and effectively.

      + Provides detailed information about the player, including attributes, skills and stats.

      + Helps users make decisions in player selection, for example in a football management game or real-life player selection.

   - Approach: Use rule-based reasoning to suggest players.
     
2. System architecture

   - The system includes 3 main components:

   - Knowledge base:
     
      + The set of events (player characteristics) is stored in the events.csv file.

      + The set of players and their details are stored in the players.csv file.

      + A set of inference rules, each of which associates a set of events with a specific player, is stored in the rules.csv file.

   - Inference tools:

      + Uses forward inference to find players that match the events (characteristics) the user has selected.

      + Go through the rules, checking whether the set of input events matches the set of events in the rule. If there is a match, the corresponding player in the rules will be included in the results list.

   - User interface:

      + Built using the Tkinter library, providing users with the following functions:

      + Select desired player characteristics.

      + See list of suggested players.

      + Add, delete, edit inference rules.

      + Add, delete, edit events (player characteristics).

3. Detailed description of components
   
   Evaluate players through:

   - General characteristics:

      + a1: Bipedal
      
      + a2: Good technique
     
      + a3: High physical strength 

      + a4: Fast speed 

      + a5: Good passing ability 

      + a6: Accurate finishing skills 

      + a7: Outstanding height 

      + a8: Young and healthy 

      + a9: Excellent defense ability 

      + a10: Long passing skills 

      + a11: Ability to predict situations well 

      + a12: Good ability to play first ball 

      + a13: Good ball control ability 

      + a14: Good leadership ability 

      + a15: Ability to react quickly 

      + a16: Good vision

   - Goalkeeper:

      + a17: Excellent reflexes

      + a18: Ability to command the defense

      + a19: High ball catching skill

      + a20: Ability to play the ball accurately

      + a21: Ball handling skills with your feet

   - Defender:

      + a22: Ability to closely mark people

      + a23: Ability to tackle effectively

      + a24: Good aerial combat skills

      + a25: Ability to support attacks

      + a26: Discipline in defense

      + Midfielder (Midfielder)

      + a27: Ability to control the pace of the match

      + a28: Accurate short passing ability

      + a29: Ability to dribble to escape pressing

      + a30: Good long passing ability

      + a31: Ability to score goals from a distance

- Forward:

   + a32: Good goalscoring instincts

   + a33: Ability to move intelligently without the shadow

   + a34: Ability to create space

   + a35: Diverse finishing skills

   + a36: Ability to choose good locations


4. Law of inference

   - Each inference rule has the form: event1, event2, ... -> player_id

   - For example: a1, a2, a3 -> b1 means that if a player has the characteristics a1, a2, a3, the system will suggest player b1.

5. Illustrative example

   - Suppose the user selects the characteristics: "Bipedal", "Good technique", "High physical strength". The system will search for rules containing corresponding events (e.g. a1, a2, a3) and suggest suitable players (e.g. b1).
