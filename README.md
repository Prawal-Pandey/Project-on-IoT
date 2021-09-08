# Bolt-IoT
An industry based project designed for temperature monitoring and alerts.

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->
<!-- wp:image -->
<figure class="wp-block-image"><img src="https://user-images.githubusercontent.com/87165116/132452735-d422cc26-4182-4cb3-baae-4ab2c8e8ae25.jpg" alt="Displaying IMG_20210902_162251.jpg"/></figure>

<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3>Idea Behind This Project </h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>An accurate determination and monitoring of temperature has become an important factor in many industries to deliver the best product.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In this project we will be monitoring the temperature of an industrial production line and will be alerting the authorities in case any problem is detected using the Bolt Cloud platform.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Things used in this project</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":3} -->
<h3>Hardware Components</h3>
<!-- /wp:heading -->

<!-- wp:list {"ordered":true} -->
<ol><li>Bolt Wi-Fi Module</li></ol>
<!-- /wp:list -->

<!-- wp:image {"id":9110,"width":349,"height":85,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large is-resized"><img src="http://projectsubmission.boltiot.com/wp-content/uploads/2021/08/47caaac-bolt_techspec-1024x250.png" alt="" class="wp-image-9110" width="349" height="85"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>2. LM35 Temperature sensor </p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7991,"width":126,"height":126,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large is-resized"><img src="http://projectsubmission.boltiot.com/wp-content/uploads/2021/07/lm35-5.jpg" alt="" class="wp-image-7991" width="126" height="126"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>3. 2 x LED</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":9333,"width":186,"height":119,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large is-resized"><img src="http://projectsubmission.boltiot.com/wp-content/uploads/2021/08/led-1.png" alt="" class="wp-image-9333" width="186" height="119"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>4. Buzzer</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":5510,"width":171,"height":171,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large is-resized"><img src="http://projectsubmission.boltiot.com/wp-content/uploads/2021/05/buzzer-1024x1024.jpg" alt="" class="wp-image-5510" width="171" height="171"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>5. Jumper Wires</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":3744,"width":187,"height":136,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large is-resized"><img src="http://projectsubmission.boltiot.com/wp-content/uploads/2021/03/jumper-wires.jpg" alt="" class="wp-image-3744" width="187" height="136"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>6. USB Cable</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":9337,"width":203,"height":129,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large is-resized"><img src="http://projectsubmission.boltiot.com/wp-content/uploads/2021/08/USB-cable.png" alt="" class="wp-image-9337" width="203" height="129"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>7. Breadboard </p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":3864,"width":182,"height":182,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large is-resized"><img src="http://projectsubmission.boltiot.com/wp-content/uploads/2021/03/breadboard_mini.jpeg" alt="" class="wp-image-3864" width="182" height="182"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3>Software and Online Services</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Bolt Cloud<img class="wp-image-9862" style="width: 150px" src="http://projectsubmission.boltiot.com/wp-content/uploads/2021/09/image.png" alt=""></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Twilio<img class="wp-image-9863" style="width: 150px" src="http://projectsubmission.boltiot.com/wp-content/uploads/2021/09/image-1.png" alt=""></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Mail-gun  <img class="wp-image-1930" style="width: 150px" src="http://projectsubmission.boltiot.com/wp-content/uploads/2021/01/Mailgun-Email.png" alt=""></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Telegram   <img class="wp-image-1343" style="width: 90px" src="http://projectsubmission.boltiot.com/wp-content/uploads/2021/01/telegram-icon.jpg" alt=""></p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Hardware Setup</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>Step 1:</strong> Take the bolt Wi-Fi module and 3 connecting wires namely ; red, orange and brown (note that you can take any 3 color wires) and insert them in 5V , A0 and GND respectively.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Step 2 :</strong> Insert the other end of the three wires in breadboard as shown in the image below.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":9850,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2021/09/Screenshot-24.png" alt="" class="wp-image-9850"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><strong>Step 3:</strong> Hold the sensor in a manner such that you can read LM35 written on it. </p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7991,"width":179,"height":179,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large is-resized"><img src="http://projectsubmission.boltiot.com/wp-content/uploads/2021/07/lm35-5.jpg" alt="" class="wp-image-7991" width="179" height="179"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>In this position, identify the pins of the sensor as VCC, Output and GND from your left to right.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Step 4 :</strong> Place the pins of sensor in breadboard in such a way that :</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>VCC pin of the LM35 is inserted in 5V slot of the breadboard (row of red wire) .</li><li>Output pin of the LM35 is inserted in A0 (Analog input pin) slot of the breadboard (row of orange wire) .</li><li>GND pin of the LM35 is inserted in GND slot of the breadboard (row of brown wire).</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":9852,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2021/09/Step_2.png" alt="" class="wp-image-9852"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><strong>Step 5 : </strong>Take another connecting wire and insert it to the Pin 0 of bolt Wi-Fi module . Place the other end of connecting wire in the breadboard as shown below:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":9853,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2021/09/Step_3.png" alt="" class="wp-image-9853"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><strong>Step 6 :</strong> Take 2 LEDs and insert their short leg in GND (brown wire) of breadboard and the long leg in Pin 0 of breadboard ( used as yellow wire).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":9854,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2021/09/Step_4.png" alt="" class="wp-image-9854"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><strong>Step 7 : </strong>Take a different connecting wire and insert it to the Pin 1 of bolt Wi-Fi module and place it's other end in the breadboard. Also, from GND of breadboard insert a connecting wire and extend it to another point in breadboard beside wire of Pin 1 of breadboard, as shown below:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":9855,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2021/09/Step_5.png" alt="" class="wp-image-9855"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><strong>Step 8:</strong> Place the long leg of buzzer in Pin 1 of breadboard and short leg in GND of breadboard. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Connect the bolt Wi-Fi module with USB cable and run the program.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong><span class="has-inline-color has-accent-color">(Note: Connect the power source with bolt Wi-Fi module only after all the circuit connects are done and rechecked to prevent any damage to the components.) </span></strong></p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":9856,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2021/09/Step_6.png" alt="" class="wp-image-9856"/></figure>
<!-- /wp:image -->

<!-- wp:image -->
<figure class="wp-block-image"><img src="https://user-images.githubusercontent.com/87165116/132453018-39b556a7-d096-4032-a24b-38cccbfe6e4a.jpg" alt="Displaying IMG_20210902_162251.jpg"/></figure>




<!-- /wp:image -->

<!-- wp:heading -->
<h2>Software Programming</h2>
<!-- /wp:heading -->

<!-- wp:list {"ordered":true} -->
<ol><li><strong>Bolt Platform</strong> </li></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Bolt IoT platform allows to control your device and collect data from IoT devices in just a couple of seconds. You can get insights by implanting programming codes to predict sensor values. To know more visit&nbsp;<a href="http://boltiot.com/">boltiot.com</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>2. Twilio Platform</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Twilio platform allows you to receive SMS alerts over the registered mobile number when the command is given to it. For further information you can visit <a rel="noreferrer noopener" href="https://www.twilio.com" target="_blank">https://www.twilio.com</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>3. Mailgun</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Mailgun empowers you with sending emails with preferred languages within a moment of time. To know more you can check <a rel="noreferrer noopener" href="https://www.mailgun.com" target="_blank">https://www.mailgun.com</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>4. Telegram</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Telegram is a free and open source, cross-platform, cloud-based instant messaging software that can be used as alert messages after creating bots. If you want to know more about this you can visit <a rel="noreferrer noopener" href="https://telegram.org" target="_blank">https://telegram.org</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>5.</strong> Working with the Codes</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now that the hardware configuration is already done, we will write the code for visualizing the temperature data received from the Bolt device and set-up the different alerts.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I have divided the code in different situation and imported the specific condition whenever they have to be initialized. This makes the code looks clean and is easy to read and detect errors in different sections if any.</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>This is the main file that we will run .</li></ul>
<!-- /wp:list -->

<!-- wp:image {"id":9858,"width":691,"height":546,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large is-resized"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2021/09/main.png" alt="" class="wp-image-9858" width="691" height="546"/></figure>
<!-- /wp:image -->

<!-- wp:list -->
<ul><li>If the temperature remains in specified minimum and maximum value and does not come across the suspicious high and low zones, it gives the output as "Temperature is being monitored and seems to be fine.</li><li>If the temperature value is found to be in specified Suspicious Low or Suspicious High, the LEDs and buzzer are turned on and off repeatedly  and alerts are sent to telegram.  (Note that if the temperature lies in suspicious high the LEDs brightly glows and buzzer produces sound to its max repeatedly while if its a suspicious low zone the LEDs glows and buzzer produces sounds with less intensity but repeatedly.)</li></ul>
<!-- /wp:list -->

<!-- wp:image {"id":9860,"width":750,"height":714,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large is-resized"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2021/09/Suspicious-1.png" alt="" class="wp-image-9860" width="750" height="714"/><figcaption>Suspicious High Condition</figcaption></figure>
<!-- /wp:image -->

<!-- wp:list -->
<ul><li>If the temperature value is found to be in Critical Low or Critical High, the LEDs and buzzer are turned on ,alerts are sent to telegram along with an SMS alert and E-mail alert sent to the owner/manager of the industry.</li></ul>
<!-- /wp:list -->

<!-- wp:image {"id":9861,"width":714,"height":947,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large is-resized"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2021/09/Critical.png" alt="" class="wp-image-9861" width="714" height="947"/><figcaption>Critical High Condition</figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>For the complete code you can follow the link to my Github account given below:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"left"} -->
<p class="has-text-align-left"><a rel="noreferrer noopener" href="https://github.com/Prawal-Pandey/Bolt-IoT/tree/main/Temprature_Monitoring" data-type="URL" data-id="https://github.com/Prawal-Pandey/Bolt-IoT/tree/main/Temprature_Monitoring" target="_blank">https://github.com/Prawal-Pandey/Bolt-IoT/tree/main/Temprature_Monitoring</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For the hardware connections, you can take help through the video demonstration uploaded on my Youtube channel <a rel="noreferrer noopener" href="https://youtu.be/eOuwAI5hrco" target="_blank">https://youtu.be/eOuwAI5hrco</a> (the video quality might be low)</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>With this low cost and handy project together with the Bolt Cloud, you can easily get the temperature values and alerts. This can be useful in an industrial environment like a Food and Beverage Processing industry where environment monitoring is of utmost importance for measuring and controlling the temperature.</p>
<!-- /wp:paragraph -->
