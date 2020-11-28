Team G

Readme Parser | WTCC CSC 130 Group Project

https://github.com/bizzlebin/team_g/

***

By Jeremiah Thomas, et al

***

Created 2020-11-16

+++
Welcome

Welcome to the project readme for our team, tentatively named Team G! This will be our "home base" for the CSC 130 group project and todo list. I will try to keep most of the key information here because we have such a small group. However, as needed, I will break out some content into other files/folders; do not modify anything outside of your scope, please.

Keep in mind that this is a public repo so we won't be posting any e-mail addresses, links to our other collaboration tools, etc. We'll have regular group meetings and some [emotion and thought] communication elsewhere but everything of substance should be committed here. By doing the majority of our work in the open on Git, we will not only have better control of versioning but something we can all share in the future on a résumé; I plan to keep this repo open and public indefinitely.

+++
Schedule

===
Week 1 (2020-11-15)

---
Due By *Tuesday* (2020-11-17)

0. Read this readme.
1. Read the readme in the resources directory.
2. Set up Slack.
2.1. Create Slack account and/or join our channel.
2.2. Say hello ASAP, including your name and *GitHub username* so you can get a repo invite!
3. Set up Git.
3.1. Create GitHub account and/or join this repo as a collaborator.
3.2. Install Git (optional; I use plain Git (it comes with Git GUI and Git Bash) as GitHub Desktop is very so-so and a privacy/update nightmare, though the integration is tighter).
3.3. Fetch repo (optional; if you you wanted, you could theoretically do all edits from GitHub...).
3.4. Create branch (optional; if you're not making breaking changes then you may commit to master).
4. Add your availability so we can schedule a regular Slack meeting (use a Git commit to the availability.txt file—get used to commits and please follow the commit message style you read about in step 1 !).
5. Pick your role in roles.txt; if you want to switch with someone before the end of Tuesday use Slack or e-mail them to discuss.
6. PM: create Readme Parser 0.3.0 (module we'll be working with).

---
Due By *Thursday* (2020-11-19)

1. RD: complete JSON integration of current [outdated] regex (fields.json).
2. UID: prototype file dialog (dialog.py).
3. AS: create plaintext of pseudocode for current algorithm (pseudocode.txt).

===
Week 2 (2020-11-22)

---
Due By *Sunday* (2020-11-22)

1. Meeting prep: 20:00 .

---
Due By *Monday* (2020-11-23)

1. RD: update JSON to new NKMF spec (eg, it should parse the project readme fully).
2. UID: convert Readme Parser output to match current NKMF spec.
3. AS: develop improved algorithm that supports multiple text chunks in queue, labeling each by NKMF subdivision name ("Title", "Authorship", etc), which can then be parsed individually for fields ("title", "version", "container", etc); dinkuses and chapter markers should signal the end of each chunk but only the content should be included in the stored text.
4. PM: create docstrings for functions.

---
Due By *Tuesday* (2020-11-24)

1. Meeting prep: 20:00 .

---
Due By *Wednesday* (2020-11-25)

1. RD:
1.1. Finish updating JSON so it captures all setuptools fields in order (eg, it should parse the project readme fully): https://gist.github.com/musashix90/697f121e49ab3a3d7c373a35efebe4ca has the old RD's work, which captures more than needed and doesn't use setuptools names but it is fairly complete.
1.2. Develop schema (with AS) for new JSON: we may need a field for the *UEWSG* division/subdivision so the parser knows where in the queue everything should be.
2. AS:
2.1. Fix regressions: """name""" should not include entire title subdivision, UEWSG names should not be put into readme, etc.
2.2. Help RD develop JSON schema.
3. PM: Create presentation outline.

---
Due By *Friday* (2020-11-27)

1. RD: rewrite regex according to new schema.
2. AS: implement new, simplified algorithm for both inserting readme into queue by UEWSG division/subdivision and parsing out of the queue for setuptools fields.
3. PM: debug remaining regressions and update docstrings.

===
Week 3 (2020-11-29)

---
Due By *Sunday* (2020-11-29)

1. Meeting prep: 20:00 .

---
Due By *Monday* (2020-11-30)

1. RD: finish all regex work ASAP and document the schema in the metadata file.
2. AS: optimize algorithm: it still needs to be less nested in order to speed up run time.
3. PM: start on group paper.

+++
Ground Rules

For now, because the group is so small, I am going to give everyone commit privileges; please avoid pull requests unless you are merging a branch with conflicts. Here are the general ground rules we'll be observing:

1. Respect others.
2. Respect others's work.
3. Respect the group roles and hierarchy.
4. Respect the project and goals.
5. Respect everyone's time—including your own.

+++
Metametadata

**meta_title**: Readme
**meta_uri**: https://github.com/bizzlebin/team_g/blob/master/team/readme.txt
**meta_author**: Jeremiah Thomas
**meta_created**: 2020-11-20
**meta_updated**: 2020-11-27