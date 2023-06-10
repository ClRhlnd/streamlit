Skip to main content

Streamlit
Style Column Metrics like the Documentation
🎈 Using Streamlit

Log In

🎈 Click here for guidelines on how to post an effective question in the forum.

Style Column Metrics like the Documentation
🎈 Using Streamlit
Dec 2021
Mar 8

Shawn_Pereira
Jan '22
Here is an example with fontawesome icons and different colours.

tmp
tmp
726×195 7.22 KB
But components are a better way to go.

Cheers.

2 Replies



snehankekre
Docs at Streamlit
Jan '22
Hi @saxon11,

Just to clarify: The Streamlit documentation is not a Streamlit app. We use Next.js, React, and Markdown to build the site and Netlify to host it. The code is public: GitHub - streamlit/docs: Source code for the Streamlit Python library documentation 242

Best, :balloon:
Snehan

1

2 months later

yeshwanth1312

Shawn_Pereira
Feb '22
Can you share the source code for this @Shawn_Pereira . Thanks




Shawn_Pereira
Feb '22
Hi @yeshwanth1312

I don’t have the earlier code as that was written just for a temporary purpose.

I have re-written the following code only for 1 kpi metric. You can do:
a. put the code in a function, so you can all it many times
b. change the parameters & variables to suit your purpose
c. use st.columns for multiple kpi metrics, etc.

# variables
wch_colour_box = (0, 204, 102)  # green
wch_colour_font = (0, 0, 0)  # blackfont
fontsize = 18
valign = "left"
iconname = "fas fa-asterisk"
sline = "Users" # kpi name
lnk = ''
i = 1000  # kpi value
htmlstr = f"""

                         {i}
                        


                    <span style='font-size: 18px;
                    margin-top: 0;'>{sline}</style>
                    </span></p>"""

st.markdown(lnk + htmlstr, unsafe_allow_html=True)


Also, pasting a snapshot of the code here, as my copy-paste makes some of my text disappear.
tstdf
tstdf
933×561 17.7 KB
Cheers

1 Reply
2

2 months later

leb_dev

Shawn_Pereira
Apr '22
Maybe it’s late but how can i get like these customized metrics?




Shawn_Pereira
Apr '22
Just try out the code given in the picture above, and then modify it for your use, as needed.

Cheers



2 months later

Oceane

Shawn_Pereira
Jul '22
Hi @Shawn_Pereira ,

I tried the code you suggested but it doesn’t work. Layout is not taken into account.
My code :
image
image
766×764 32.3 KB
Result :
image

Thanks




Shawn_Pereira
Jul '22
Hi @Oceane

I suggest that you:

properly duplicate my code
then check if it works for you
and thereafter modify it to suit your needs
At first glance, I see some errors in your code:

The lnk variable is missing
‘order-radius’ should be ‘border-radius’
the last link (markdown) does not have the lnk variable as in my code
Lastly, you will have to work with the available streamlit layouts. Use columns, containers, etc. You would need to do a little experimenting.

Here’s the demo code, if you want to copy-paste:

import streamlit as st

wch_colour_box = (0,204,102)
wch_colour_font = (0,0,0)
fontsize = 18
valign = "left"
iconname = "fas fa-asterisk"
sline = "Observations"
lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
i = 123

htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                              {wch_colour_box[1]}, 
                                              {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p>"""

st.markdown(lnk + htmlstr, unsafe_allow_html=True)
Cheers

1

8 months later

Lazy
Mar 8
Thank you very much sir .

1

 This topic will close a year after the last reply.
Hello! Looks like you’re enjoying the discussion, but you haven’t signed up for an account yet.
Tired of scrolling through the same posts? When you create an account you’ll always come back to where you left off. With an account you can also be notified of new replies, save bookmarks, and use likes to thank others. We can all work together to make this community great. heart


Sign Up
Maybe later
no thanks
Suggested Topics
Topic	Replies	Views	Activity
Allow user to add any number of elements to a page
🎈 Using Streamlit
4	246	Sep '22
I am not able to deploy my app through remote server however it was working fine with local system
🎈 Using Streamlit
3	297	Nov '22
Traceback error
🎈 Using Streamlit
windows
3	337	Jan 27
Want to read more? Browse other topics in 
🎈 Using Streamlit
 or view latest topics.
​
    
import streamlit as st

wch_colour_box = (0,204,102)
wch_colour_font = (0,0,0)
fontsize = 18
valign = "left"
iconname = "fas fa-asterisk"
sline = "Observations"
lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
i = 123

htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                              {wch_colour_box[1]}, 
                                              {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p>"""

st.markdown(lnk + htmlstr, unsafe_allow_html=True)

  
