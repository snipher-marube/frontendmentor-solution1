# Frontend Mentor - Multi-step form

![Design preview for the Multi-step form coding challenge](https://github.com/snipher-marube/frontendmentor-solution1/blob/main/static/screenshot/preview.png)

## Welcome! 👋

Thanks for checking out this front-end coding challenge.

[Frontend Mentor](https://www.frontendmentor.io) challenges help you improve your coding skills by building realistic projects.

**To do this challenge, you need a good understanding of HTML, CSS and JavaScript.**

## The challenge

Your challenge is to build out this multi-step form and get it looking as close to the design as possible.

You can use any tools you like to help you complete the challenge. So if you've got something you'd like to practice, feel free to give it a go.

Your users should be able to:

- Complete each step of the sequence
- Go back to a previous step to update their selections
- See a summary of their selections on the final step and confirm their order
- View the optimal layout for the interface depending on their device's screen size
- See hover and focus states for all interactive elements on the page
- Receive form validation messages if:
  - A field has been missed
  - The email address is not formatted correctly
  - A step is submitted, but no selection has been made

Want some support on the challenge? [Join our Slack community](https://www.frontendmentor.io/slack) and ask questions in the **#help** channel.

## installation and setup

- Clone the repo `git clone https://github.com/snipher-marube/frontendmentor-solution1.git`
- Change directory `cd frontendmentor-solution1`
- Create a virtual environment `python3 -m venv venv`
- Activate the virtual environment `source venv/bin/activate`
- Install dependencies `pip install -r requirements.txt`
- Run the app `python manage.py runserver`

## configure Tailwindcss

- start the tailwindcss build process `python manage.py tailwind start`
- build the tailwindcss `python manage.py tailwind build`

## Deploy to Heroku

- Create a Heroku account
- Install Heroku CLI
- Login to Heroku `heroku login`
- Create a Heroku app `heroku create`
- Add the app to git `git remote add heroku https://git.heroku.com/your-app-name.git`
- Push to Heroku `git push heroku main`
- Run migrations `heroku run python manage.py migrate`
- Create a superuser `heroku run python manage.py createsuperuser`
- Open the app `heroku open`


## Deploy to Vercel

- Create a Vercel account
- Install Vercel CLI
- Login to Vercel `vercel login`
- Create a Vercel app `vercel create`
- Push to Vercel `vercel --prod`
- Run migrations `vercel run python manage.py migrate`
- Create a superuser `vercel run python manage.py createsuperuser`
- Open the app `vercel open`

## Fun jokes

- What do you call a snake that is 3.14 meters long? A πthon.
- Why did the Python programmer not respond to the foreign mails he got? Because his interpreter was busy collecting garbage.

## Feedback

Feedback is always welcome, so if you have any to give on this challenge please email [
  sniphermarube[at]gmail[dot]com
](mailto:sniphermarube[at]gmail[dot]com).