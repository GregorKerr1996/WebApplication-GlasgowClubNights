switch (new Date().getDay()) {
//SUNDAY
            case 0:
                var sun1 = document.createElement("IMG");
                sun1.src = "{{ MEDIA_URL }}subclub.jpg";
                sun1.alt = "subclub";
                document.getElementById('first').appendChild(sun1);
                document.getElementById('cap1').innerHTML = "<a href=\"{% url 'subclub' %}\">Subclub Sundays</a>";
                var sun2 = document.createElement("IMG");
                sun2.src = "{{ MEDIA_URL }}bamboo.jpg";
                sun2.alt = "bamboo";
                document.getElementById('second').appendChild(sun2);
                document.getElementById('cap2').innerHTML = "<a href=\"{% url 'bamboo' %}\">Disco Badger</a>";
                var m3 = document.createElement("IMG");
                sun3.src = "{{ MEDIA_URL }}lacheetah.jpg";
                sun3.alt = "lacheetah";
                document.getElementById('third').appendChild(sun3);
                document.getElementById('cap2').innerHTML = "<a href=\"{% url 'la_cheetah' %}\">Sundays @ La Cheetah</a>";

                document.getElementById('carousel-header').innerHTML = "Check out the biggest nights for Sunday!";
                break;

//MONDAY
            case 1:
                var mon1 = document.createElement("IMG");
                mon1.src = "{{ MEDIA_URL }}viper.jpg";
                mon1.alt = "viper";
                mon1.usemap = "mon1"
                document.getElementById('first').appendChild(mon1);
                document.getElementById('cap1').innerHTML = "<a href=\"{% url 'viper' %}\">Monday Night Heat</a>";

                var mon2 = document.createElement("IMG");
                mon2.src = "{{ MEDIA_URL }}kokomo1.jpg";
                mon2.alt = "kokomo";
                document.getElementById('second').appendChild(mon2);
                document.getElementById('cap2').innerHTML = "<a href=\"{% url 'kokomo' %}\">Mile High Monday</a>";

                var mon3 = document.createElement("IMG");
                mon3.src = "{{ MEDIA_URL }}polo.jpg";
                mon3.alt = "polo";
                document.getElementById('third').appendChild(mon3);
                document.getElementById('cap3').innerHTML = "<a href=\"{% url 'polo' %}\">Back Door</a>";

                document.getElementById('carousel-header').innerHTML = "Check out the biggest nights for Monday!";
                break;
//TUESDAY
            case 2:
                var tues1 = document.createElement("IMG");
                tues1.src = "{{ MEDIA_URL }}kushion.jpg";
                tues1.alt = "kushion";
                document.getElementById('first').appendChild(tues1);
                document.getElementById('cap1').innerHTML = "<a href=\"{% url 'kushion' %}\">Juicy Tuesday</a>";

                var tues2 = document.createElement("IMG");
                tues2.src = "{{ MEDIA_URL }}subclub.jpg";
                tues2.alt = "subclub";
                document.getElementById('second').appendChild(tues2);
                document.getElementById('cap2').innerHTML = "<a href=\"{% url 'subclub' %}\">I AM @ Subclub</a>";

                var tues3 = document.createElement("IMG");
                tues3.src = "{{ MEDIA_URL }}polo.jpg";
                tues3.alt = "polo";
                document.getElementById('third').appendChild(tues3);
                document.getElementById('cap3').innerHTML = "<a href=\"{% url 'polo' %}\">Text Me Tuesdays</a>";

                document.getElementById('carousel-header').innerHTML = "Check out the biggest nights for Tuesday!";
                break;
//WEDNESDAY
            case 3:
                var wed1 = document.createElement("IMG");
                wed1.src = "{{ MEDIA_URL }}shimmy.jpg";
                wed1.alt = "shimmy";
                document.getElementById('first').appendChild(wed1);
                document.getElementById('cap1').innerHTML = "<a href=\"{% url 'shimmy' %}\">No Way Wednesdays</a>";

                var wed2 = document.createElement("IMG");
                wed2.src = "{{ MEDIA_URL }}bamboo.jpg";
                wed2.alt = "bamboo";
                document.getElementById('second').appendChild(wed2);
                document.getElementById('cap2').innerHTML = "<a href=\"{% url 'bamboo' %}\">W N B</a>";

                var wed3 = document.createElement("IMG");
                wed3.src = "{{ MEDIA_URL }}cathouse.jpg";
                wed3.alt = "cathouse";
                document.getElementById('third').appendChild(wed3);
                document.getElementById('cap3').innerHTML = "<a href=\"{% url 'cathouse' %}\">Beast Wednesdays</a>";

                document.getElementById('carousel-header').innerHTML = "Check out the biggest nights for Wednesday!";
                break;
//THURSDAY
            case 4:
                var thurs1 = document.createElement("IMG");
                thurs1.src = "{{ MEDIA_URL }}hive.jpg";
                thurs1.alt = "hive";
                document.getElementById('first').appendChild(thurs1);
                document.getElementById('cap1').innerHTML = "<a href=\"{% url 'hive' %}\">Hive Thursdays</a>";

                var thurs2 = document.createElement("IMG");
                thurs2.src = "{{ MEDIA_URL }}garage2.jpg";
                thurs2.alt = "garage";
                document.getElementById('second').appendChild(thurs2);
                document.getElementById('cap2').innerHTML = "<a href=\"{% url 'garage' %}\">Element Thursdays</a>";

                var thurs3 = document.createElement("IMG");
                thurs3.src = "{{ MEDIA_URL }}kokomoclub.jpg";
                thurs3.alt = "kokomo";
                document.getElementById('third').appendChild(thurs3);
                document.getElementById('cap3').innerHTML = "<a href=\"{% url 'kokomo' %}\">Party Monster</a>";

                document.getElementById('carousel-header').innerHTML = "Check out the biggest nights for Thursday!";
                break;
//FRIDAY
            case 5:
                var fri1 = document.createElement("IMG");
                fri1.src = "{{ MEDIA_URL }}kushionWorking.jpg";
                fri1.alt = "kushion";
                fri1.href = "gcn/kushion.html"
                document.getElementById('first').appendChild(fri1);
                document.getElementById('cap1').innerHTML = "<a href=\"{% url 'kushion' %}\">Milk Fridays</a>";

                var fri2 = document.createElement("IMG");
                fri2.src = "{{ MEDIA_URL }}bambooclub.jpg";
                fri2.alt = "bamboo";
                document.getElementById('second').appendChild(fri2);
                document.getElementById('cap2').innerHTML = "<a href=\"{% url 'bamboo' %}\">Get Loose Fridays</a>";

                var fri3 = document.createElement("IMG");
                fri3.src = "{{ MEDIA_URL }}viper.jpg";
                fri3.alt = "viper";
                document.getElementById('third').appendChild(fri3);
                document.getElementById('cap3').innerHTML = "<a href=\"{% url 'viper' %}\">FOMO</a>";

                document.getElementById('carousel-header').innerHTML = "Check out the biggest nights for Friday!";
                break;

//SATURDAY
            case 6:
                var sat1 = document.createElement("IMG");
                sat1.src = "{{ MEDIA_URL }}subclub.jpg";
                sat1.alt = "subclub";
                sat1.href = "gcn/subclub.html"
                document.getElementById('first').appendChild(sat1);
                document.getElementById('cap1').innerHTML = "<a href=\"{% url 'subclub' %}\">Subculture</a>";

                var sat2 = document.createElement("IMG");
                sat2.src = "{{ MEDIA_URL }}hive.jpg";
                sat2.alt = "hive";
                document.getElementById('second').appendChild(sat2);
                document.getElementById('cap2').innerHTML = "<a href=\"{% url 'hive' %}\">Switch Saturdays</a>";

                var sat3 = document.createElement("IMG");
                sat3.src = "{{ MEDIA_URL }}garage.jpg";
                sat3.alt = "garage";
                document.getElementById('third').appendChild(sat3);
                document.getElementById('cap3').innerHTML = "<a href=\"{% url 'garage' %}\">I <3 Garage Saturdays</a>";

                document.getElementById('carousel-header').innerHTML = "Check out the biggest nights for Saturday!";
        }