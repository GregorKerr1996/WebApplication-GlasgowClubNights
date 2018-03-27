//Redirects user to relevant page if their search value matches a club page

function search(){
    var input = document.getElementById('search');

    //List of club for user input to be searcdhed against
    var clubs = ["bamboo", "cathouse", "firewater", "garage", "hive", "kokomo", "kushion", "lacheetah", "mango", "polo", "sanctuary", "shimmy", "subclub", "swg3", "viper"];
    var filter = input.value.toLowerCase();

    //Validation loop
    var valid = false;
    for (var i = 0; i < clubs.length; i++) {
        if (clubs[i].valueOf() === filter.valueOf()) {
            valid = true;
            break;
        }
        if (valid === true) {
            window.location.href = '/gcn/'+filter; //Redirects user to another window
        } else {
            window.confirm('Your search has not matched the name of a club in our Repo, please try again.');

        }
}