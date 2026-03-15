# core goal

Make a web app that acts a place that makes nfl analysis really accessible, to get the true story of teams and games quickly.

### Problem

Most NFL stats lack context, dont have much thought, and a randomly shown. For instance, if a team has 4.5 yards per play, is that good or bad? is that correlated with success?

Additionally, much NFL stats discourse revolves arounds cool sounding statistics but theres no real analysis if the stat means anything, or what it means. EPA over expected sounds good, but is it telling me anything other than EPA? Maybe but nobody has that kind of shown.

### Implication

It becomes really hard to get a sense of a team quickly. Say your favorite team is playing a team from the opposite conference, that you havent seen play. What are they good at? What are they bad at? What do they try to do? 

Coaches can typically answer that question because they do a ton of research, but for the general public its hard to get far beyond this team is "good" or "bad".

### Solution

A set of data tools that consisely show how a team has performed (overall, and in relevant component parts), how that compares to the league, and game by game. Each statistic should be backed some analysis that shows that this is a relevant thing to track. 

The tool should also show information about choices - eg does the team prefer to run or pass on 3rd down? Do they blitz, and if they do when? Finally, how do they perform relative to those choices?

### Potential Outputs

- A data dashboard that makes it easy to quickly get and understand the above information
- Narrative driven analysis (maybe similar to a jupyter notebook or a blog post) - proving a particular point. Inspiration here would be NYT/WSJ data articles.
- little "cards" in other words pieces of information (visuals, infogrpachics) that quickly standardize a team or game. The main inspirations here is video games data viz, which tend to do a better job of quickly summarizing and contextualizing key data relative to the game.

### Principles

- context context context - always explain why a metric matters, and whether its good or not
- no random data points for the hell of it


Tech
- NFL FastR is going to be the main data set given its comprehensiveness and reliability. may add others, but we will do a lot with this first
- Python based tools - most of the code should be written in python and sql. Want to avoid excessive javascript because i dont really know it. We will use R for nfl fastr for database updates, which i would like to automate.
- the web app could be django or streamlit. django offers better user account management and hosting, streamlit would be simpler.
- visualization - leaning towards python standards (matplotlib/seaborn/plotly, etc) instead of esoteric tools that are ocmplicated, but could be open.
- id want a pretty easy way to do some blog posts too. typically in the past this looks like me exploring around some data (like some of the jupyter notebooks in this repo) then translating it into a blog post/analysis.

## Ideas

"cards" for a team that show consisely what they are good at, what they are not good at, and what choices they make

## Analysis Ideas

- Figure out all the tendencies (choices) of each team. Do they blitz, do they throw deep or short, do they run on first down, do they run inside or outside, do they play man or zone, what kinds of fronts and packages do they use.


