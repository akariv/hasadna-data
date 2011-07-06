var Hasadna = (function () { 
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

    function DBServerGetHtml(path,params,elementId) {
    	$.get(APIServer+path,
    		  params,
			  function (data) {
				 $("#"+elementId).html(data);
			  },"html");
    }

    my.getRecord = function(path,callback) {
    	var params = { "o"	   : "jsonp" };
    	DBServerGetJson(path,params,callback);
    }
    
    my.findRecords = function(path,callback,spec,fields,start,limit) {
    	var params = { "o"	   : "jsonp" };
    	if ( spec != undefined ) { params["query"] = spec; }
    	if ( fields != undefined ) { params["fields"] = fields; }
    	if ( start != undefined ) { params["start"] = start; }
    	if ( limit != undefined ) { params["limit"] = limit; }
    	DBServerGetJson(path,params,callback);
    }

    my.loadRecordTemplate = function(path,elementId,template) {
    	var params = { "o"	   : "template:"+template };
    	DBServerGetHtml(path,params,elementId);
    }

    my.loadRecordsTemplate = function(path,elementId,template,spec,fields,start,limit) {
    	var params = { "o"	   : "template:"+template };
    	if ( spec != undefined ) { params["query"] = spec; }
    	if ( fields != undefined ) { params["fields"] = fields; }
    	if ( start != undefined ) { params["start"] = start; }
    	if ( limit != undefined ) { params["limit"] = limit; }
    	DBServerGetHtml(path,params,elementId);
    }

    // Tagging
    my.loadTagsForRecord = function(path,elementId) {
    	spec = { "reference" : path };
    	my.loadRecordsTemplate("/data/common/tags",elementId,"detail",spec);
    }
    	
    return my; 
}());

var H = Hasadna();