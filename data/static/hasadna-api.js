var H = (function () { 
    var my = {}, 
    	APIServer = "http://api.yeda.us"; 

    // Low Level API
    
    function DBServerGetJson(path,params,callback) {
    	$.get(APIServer+path,
      		  params,
      		  function (data) {
      			 callback(data);
      		  },"jsonp");    	
    } 

    function DBServerGetHtml(path,params,elementId,callback) {
    	$.get(APIServer+path,
    		  params,
			  function (data) {
				 $("#"+elementId).html(data);
				 if ( callback != undefined ) }
				 	callback($("#"+elementId));
    			 }
			  },"jsonp");
    }

    my.getRecord = function(path,callback) {
    	var params = { "o"	   : "jsonp" };
    	DBServerGetJson(path,params,callback);
    }
    
    my.findRecords = function(path,callback,spec,fields,start,limit) {
    	var params = { "o"	   : "jsonp" };
    	if ( spec != undefined ) { params["query"] = JSON.stringify(spec); }
    	if ( fields != undefined ) { params["fields"] = fields; }
    	if ( start != undefined ) { params["start"] = start; }
    	if ( limit != undefined ) { params["limit"] = limit; }
    	DBServerGetJson(path,params,callback);
    }

    my.countRecords = function(path,callback,spec,fields,start,limit) {
    	var params = { "o"	   : "jsonp",
    			       "count" : "1" };
    	if ( spec != undefined ) { params["query"] = JSON.stringify(spec); }
    	if ( fields != undefined ) { params["fields"] = fields; }
    	if ( start != undefined ) { params["start"] = start; }
    	if ( limit != undefined ) { params["limit"] = limit; }
    	DBServerGetJson(path,params,callback);
    }

    my.loadRecordTemplate = function(path,elementId,template,callback) {
    	var params = { "o"	   : "templatep:"+template };
    	DBServerGetHtml(path,params,elementId,callback);
    }

    my.loadRecordsTemplate = function(path,elementId,template,spec,fields,start,limit,callback) {
    	var params = { "o"	   : "templatep:"+template };
    	if ( spec != undefined ) { params["query"] = JSON.stringify(spec); }
    	if ( fields != undefined ) { params["fields"] = fields; }
    	if ( start != undefined ) { params["start"] = start; }
    	if ( limit != undefined ) { params["limit"] = limit; }
    	DBServerGetHtml(path,params,elementId,callback);
    }

    // Header
    my.loadLoginHeader = function(elementId) {
    	my.loadRecordTemplate("/data/",elementId,"login-header");
    }
    
    // Tagging
    my.loadTagsForRecord = function(path,elementId) {
    	spec = { "reference" : path };
    	my.loadRecordsTemplate("/data/common/tags",elementId,"snippet",spec);
    }
    	
    return my; 
}());
