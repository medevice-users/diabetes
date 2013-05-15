## Actors, Contexts, Goals Report 
  - A tool for documenting learning about the actor’s problems, contexts, and goals
  - Techniques: using contextual/situational observation, shadowing, immersion
  - Model who, what, where, when, and why?  (but not how)
  - Use the “five whys?” technique to get to root causes
  - Document goals, expectations, experiences, desires, language used, mental models, emotions
  - Include context, time and place of use, compliments, frequency, interruptions, the whole session
  - What decisions are the actors trying to make?
  - Aim to understand pain points, current anti-scenarios, new opportunities, cues in environment
  - Don’t specify specific implementation or interface details or any non-user visible elements
  
## Goal Description List “what the actors really want”
  - List of the goals discovered above
  - E.g. “get caught up on the day’s correspondence” or “help this patient control her glucose better”

  - An example of finding goals and activities:
    - Q1: Why is the PCP looking at this blood glucose heatmap graph? A: Because the pt. in this visit has signs of poor control and a single data point or her verbal description is not enough data.
    - Q2: Why signs of poor control? A2: Damage from too high blood glucose.
    - Q3: Why too high blood glucose? A3: Something is spiking it. Maybe something in diet?
    - Q4: Why is it spiking on these days and times? A4: Ask patient about context of high outliers.

    - Goal (for list): Easily see and ask about all the high outliers. 

    - Generated activity design ideas:
1) Clearly highlight high and low outliers in the graphs
2) List each event clearly in a separate table
3) Add a simple filtering control to focus on high or low or both types of outliers

    - Some anti-goals: “Make it 'cool'”, “use this technology”, “What would Steve Jobs would do?”

research above
-----
design below



## Design Document “the solution”
### Activity Description List (a.k.a. idealized scenarios or workflows)
 
Tasks are situations with a single, well-specified goal, such as "respond to this email." Activities are larger groupings, comprised of multiple tasks that fit together, such as "get caught up on the day's correspondence" which means reading email, responding, looking up information, sometimes to copy and paste into emails, checking calendars, and other associated, related tasks. 

  - Complete list of high-level, goal-oriented activities from actor’s POV in realistic context
  - Specify link to an actor’s goal discovered above.
  
   - E.g. (activity from the goal "easily see and ask patient about all the high outliers" from above):
    - Filter out all data except for the high outliers using filter checkboxes
    - (Adjust high side of slider that defines "normal" range for this pt to see more near-outlier events)
    - Look at table listing events (be able to sort events by datetime or value).
    - For each event in table, have a space to add an annotation (and easily move back and forth, with the keyboard) to enter additional data for each event.
    - Possibly add flags or tags to make visualization, search and sort easier.
	
  - “This is where design begins” - Hoekman
  - Use “pretend it’s magic/legal/from the future” and “pretend it’s a great human assistant”
  - Suggestion: specify one for each major activity per core actor
  - Think of: an iPod 1.0 and Ford Model T: an imperfect Minimum Viable Product

### Activity - Use Case Map (optional) “the link from the solution to specifics”
  - Hierarchical: activities, tasks, actions, operations
  - The bridge between high-level “activity descriptions” and low-level “use cases”  
   - See Hoekman’s example at bottom
## Use Case List “the specifics”
  - Step-by-step specification of task accomplished by one or more actors
  - Idealized functionality, behavior, presentation, interaction from an actor’s POV
  - Keep them simple, short, “agile”, `<10` steps, at actor’s level
  - Also a record of specific design decisions
  - Write them incrementally, at just-enough precision, and just-in-time
  - A UC Template:
    - Name
    - Short summary
    - The actor(s) and context
    - The linked activity and goal
    - Step 1
    - Step ...
    - Step n
    - Also exceptions, when problems occur, novel situations, bad data, wrong sequence, etc.
    - Optional: include implementation and/or design details inline, but keep clearly separated
    - See Hoekman, Designing the Obvious 2nd Edition, p. 68-74

## Task-flow Diagrams (optional)
  - See Hoekman p. 74-75 and Norman

## Wireframes (optional)
  - E.g. protoshare

## Design Description Document (optional)
  - Single doc that combines wireframes and use cases on a single page
  - http://thinkvitamin.com/business/deliverables-that-work-design-description-documents/

## Other Documents
- “Nice to Have” and Non-features List - to keep us honest :)
- Hypotheses Doc
- Ideas Doc

## References
- Hoekman “Designing the Obvious” 2nd edition
http://www.peachpit.com/guides/content.aspx?g=webdesign&seqNum=358
- Cooper “About Face 3”
- Reis "The Lean Startup", Blank "4 Steps", "Startup Owner's Manual"
- Lean Startup ideas: MVP, separate product, customer, and market hypotheses for testing
(ideas) -> build -> (code) -> measure -> (data) -> learn -> (ideas) -- minimize total time through the loop
- Can't set a deadline on fit
- and "follow the love"

Activity grid example:
http://ptgmedia.pearsoncmg.com/images/irf_guide_webdesign_evans/elementLinks/021508fig01.jpg

