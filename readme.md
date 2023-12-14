This is my project with Caran d'Ache on the future of drawing, where we have to make a playful AI creative assistant. 

Current name of my assistant is Snailed-it.

Below is the devlog with my day-to-day progress. Enjoy.

# DevLog

## 2023-12-14

Test day results

![test-day](/process/2023-12-14/IMG_5798.JPG)

1. It is still not very obvious that you need to take an object and put it on my device. In most cases I had to tell people that the snail was apart of the experience. In the second session, I tried putting it in a box right next to the device. Still unclear. Probably, having a group of objects will make things clearer. In addition, I need to try putting objects on some kind of a platform made of the same material as the square for positioning objects on the device.

2. The device is perceived as a lamp. Still need to think if that is the impression I want.

3. Blank buttons were not clear at all. Only one tester was curious enough to explore them without any explanation. Buttons with icons made more sense. Even though the icons were not always very understandable, they at least sparked some interest. Buttons with text are probably too in the face, but at the same time still not super clear. Will probably keep buttons with icons, but will reconsider the icons.

4. An interesting insight is that the first three buttons (outline, shapes, shading) are associated together. Some people saw them as different layers of one image. Meanwhile, the random button is a very fun option, but is a bit apart. So, the idea now is to group the three first buttons together and distinguish "random" from them (by color or shape and distance).

5. When clicking on the random button again, people expect a new random image.

6. What if you put two objects?

TBC

## 2023-12-07

Need to think about the way I can cover power cables, because there will be one from the projector and one from the Raspberry Pi. Probably can put them in some textile with velcro.

Added necessary [steps](/process/2023-12-07/steps.md) for completing the project.

Talked to the guy from the Metal Pool. They have all sorts of steel tubes and plates, so basically it is up to me to decide on the size and thickness. Will need to finish my 3D model BEFORE THE HOLIDAYS, so that he can order necessary materials if needed. And straight after the holidays we will start production (Jan 8). The gravure of the text for my parameters can be made at the Prototype Pool.

His suggestion on how to do the base and fix the leg to it:
![suggestion_1](/process/2023-12-07/IMG_5736.JPG)
![suggestion_2](/process/2023-12-07/IMG_5737.JPG)
There will be a short large tube soldered to the base and the main tube will go inside and will be fixed with screws/bolts. The base is hollow, so that I can fit my electronics in it.


Need to think if I actually want to make a wooden prototype first. Probably only for some details. 

## 2023-12-06

Made first detailed sketch of my object. ![sketch](/process/2023-12-06/IMG_5729.JPG)

Since the projector is quite heavy (820g), the leg and the base should be metal, so that the object does not fall. The projector will be attached to the leg with three disks and a bolt. ![disks](/process/2023-12-06/IMG_5730.JPG) The shell of the head will be 3D printed, since it will allow to have a light top, probably with two parts. One part with holes for ventilation, because the projector heats up easily. Unfortunately, the object will have to be taller than I wanted (around 700mm), so that the projection is not too blurry. ![construction](/process/2023-12-06/IMG_5726.JPG)

Got a Raspberry Pi, SD card and cables from Pablo.

## 2023-12-05

Chose my electronic components:

- [RFID](https://www.distrelec.ch/fr/module-de-lecture-et-ecriture-rfid-compatible-arduino-13-56mhz-velleman-wpi405/p/30260977?trackQuery=rfid&pos=4&origPos=4&origPageSize=50&track=true&sid=e090ff711361566ede42bd989306aabde878056b&itemList=search) reader
- [NFC](https://www.adafruit.com/product/360) tags
- [Raspberry](https://www.adafruit.com/product/4292) Pi 4 Model B - 2 GB RAM 
- 3 soft [buttons](https://www.adafruit.com/product/3101)
- potentiometer with a metal [knob](https://www.adafruit.com/product/2058)
- projector (ideally Pico projector because it is small and light, but for now I have [this](https://www.amazon.com/Projector-Magcubic-Keystone-Correction-Portable/dp/B0C84JLZ9K?th=1) )
- [camera](https://www.adafruit.com/product/5657) (in a perfect world)

## 2023-12-04

Talked to Pierre and Laure. For the simplicity, it makes sense to use an NFC reader instead of a camera for object detection, as well as predetermined objects with NFC tags. Otherwise, it is going to take ages to teach the AI to recognize random objects.

Tried to make a quick 3D sketch in Fusion ![3d_sketch](/process/2023-12-04/Screenshot%202023-12-05%20at%2010.29.41.png) Kinda looks like a tomb stone..

Discussed possible shapes with Laure. Since, I am going to use NFC tags, I do not really need to make a box for putting objects. It can be just a flat surface. ![shape](/process/2023-12-04/231204_daria.jpg) In any case, the shape will be largely determined by my electronic components. Need to think about materials.

## 2023-12-01

Tried RGB LED light ![RGB_LED_1](/process/2023-12-01/Screenshot%202023-12-05%20at%2010.07.20.png) ![RGB_LED_2](/process/2023-12-01/Screenshot%202023-12-05%20at%2010.07.34.png) ![RGB_LED_3](/process/2023-12-01/Screenshot%202023-12-05%20at%2010.07.48.png)

## 2023-11-30

Started learning Fusion. It is actually not that difficult, much easier than Blender and Cinema 4D. Made a pencil sharpener model ![sharpener_1](/process/2023-11-30/pencil_sharpener%20v4.png) ![sharpener_2](/process/2023-11-30/pencil_sharpener%20v4_2.png)

## 2023-11-29

More electronics. Learnt how to use PIEZO ![piezo](/process/2023-11-29/Screenshot%202023-12-05%20at%2010.08.48.png)

Experimented with a light sensor ![light_sensor_1](/process/2023-11-29/Screenshot%202023-12-05%20at%2010.08.17.png) ![light_sensor_2](/process/2023-11-29/Screenshot%202023-12-05%20at%2010.08.28.png) and with a servo motor ![servo](/process/2023-11-29/Screenshot%202023-12-05%20at%2010.08.02.png)

## 2023-11-28

Now I know how to use a potentiometer and buttons. For buttons there is an internal resistor, that should be turned on via the code. This simplifies things. 

## 2023-11-27

Started learning electronics and how to use Arduino. Made SOS in Morse code with an LED.

## 2023-11-25

Added electronics scheme ![scheme](/electronics/scheme.JPG)

## 2023-11-16

Had mid [presentation](/presentations/HEAD-MD1_Caran-d-Ache_Daria-Kotova_Snailed-it.pdf) with Caran d'Ache.

Feeling awesome afterwards. On Monday morning I felt very frustrated and anxious, because I did not know if my idea made sense and was doable. But after several feedbacks on Monday, Wednesday and today, I feel quite reassured and somewhat relieved. I am also happy to finally understand what exactly I want to do. My project now has a mystery aspect, which I wanted to introduce but did not know how.

I sensed some excitement from Laure whenever she started asking if you can put my object on the table or on the floor or wherever. Do not know if Sophie liked it, she asked some clarifying question about the learning aspect, but I guess that is the topic that interests her in general.

Insights from this week: I need to plan wisely and the most important one is that I should ask for some feedback before judging myself (dah).

No idea how to start the electronics and how to improve my prototype but I will just trust the process and go with the flow. Peace.

## 2023-11-15

Finished slides for mid-presentation. Changed the name of the project to Snailed-it. Snailed-it because you nailed it :) but also because of the snail ![snail](/process/2023-11-15/camphoto_1804928587%202.JPG)

Also did some [user tests](/process/2023-11-15/user-tests/) for my last prototype, generated [Midjourney](/process/2023-11-15/midjourney/) illustrations to show the possible weirdness of AI's interpretations, as well as created various projection [outputs](/process/2023-11-15/output/).

## 2023-11-14

Today I made a new paper prototype based on Laure's feedback. It kinda looks like a phone-scuba-diving thiny. ![prototype](/process/2023-11-15/paper-prototypes-for-pres/IMG_5265.JPG)

## 2023-11-13

Cried a bit in the toilet. Am I even a designer? What a beginning to the week.

[Tested](/process/2023-11-13/user-tests/) Kick-starter. Apparently, having an assistant that you need to wake up is not obvious and very confusing. Abandonned this idea. Also, need to make it OBVIOUS that you need to put an object somewhere.

Had feedback from Laure, really helped and lifted up my spirit. Why does the assistant have to draw the outline for you if it can just project it. Genius. Can also have several options, like outline, decompose, magic (to add more stuff) and random (to randomize the output and add some spice). Feeling much better. Maybe I am a designer.

## 2023-11-12

**Pitch (what, who, where, and how), first version.**

Kick-starter is an assistant that helps people start drawing using the outlines of small objects around them. It is designed for people looking to occupy their free time. These people are open to drawing but do not know where or how to start. Kick-starter can be used at home, in the office or even at school. Simply place it on a sheet of paper and choose a small object to use as the basis for your future drawing. After analysing your object, Kick-starter draws its outline, which you can then use to kick-start your drawing.


**User journey**

![kick-starter-user-journey](/process/2023-11-12/kick-starter-user-journey.jpg)

**Key insights**
1. There is existential boredom, when people have suddenly a lot of free time and they are looking for ways to occupy themselves.
2. A lot of people do not mind drawing but they do not know what to draw and how to start.
3. Some people feel bored when they are alone. Drawing in a collaboration can be more fun.

**Next steps**





## 2023-11-11

Made a paper prototype of [Kick-starter](/process/2023-11-11/kick-starter) - an assistant that allows you to draw the outlines of small objects and thus start a drawing.

![kick-starter-1](/process/2023-11-11/kick-starter/IMG_5220.JPG)

## 2023-11-07

Prototype idea: the assistant detects if you put something on the paper, it then immediately rushes to the object and starts drawing around it. Drawing with negative space.

![negative_space_1](/process/2023-11-07/IMG_5207.jpg) ![negative_space_2](/process/2023-11-07/IMG_5208.jpg) 

## 2023-11-03

Why do I focus on textures? My assistant could help to draw whatever you want. You put something inside it, choose what outcome you want (complexity) and it scans the object and then draws it based on your settings. Thus it invites you to explore the world around you and helps you to overcome the initial creative block ("I do not mind drawing but I do not know what to draw and how").

![prototype_3](/process/2023-11-03/IMG_5205.jpg)

It can say: "Show me the world and I will show you how to draw it", "I want to learn more!.




## 2023-11-01

Continued doing [texture](/process/2023-11-01/textures-new-tests) and [sound](/process/2023-11-01/sound-tests) tests. Decided not to persue with [tastes](/process/2023-11-01/taste-tests) and sounds.

Made two prototypes: [texture-to-brush hand](/process/2023-11-01/texture-to-brush-hand) ![texture-to-brush hand](/process/2023-11-01/texture-to-brush-hand/IMG_5010.jpg) and [texture-to-image convertor](/process/2023-11-01/texture-to-image-convertor).

![texture-to-image convertor](/process/2023-11-01/texture-to-image-convertor/IMG_5017.JPG)

Need to think on how to add the mystery/exploration aspect to the assistant.