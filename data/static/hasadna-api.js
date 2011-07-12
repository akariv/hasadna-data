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
				 if ( callback != undefined ) {
				 	callback($("#"+elementId));
    			 }
			  },"jsonp");
    }

    function DBServerPostJson(path,data,callback) {
        $.ajax( APIServer+path+"?o=json",
        		{ data: data,
        	      contentType : "application/json",
        	      complete: function (ret) {
      		         			if ( callback != undefined ) {
      		         				callback(ret);
      		         			}
          	    			}, 
          	      dataType: "json",
          	      processData: false,
          	      type: "POST" }
          	      );    	
    } 

    function DBServerDelete(path,callback) {
        $.ajax( APIServer+path+"?o=json",
        		{ complete: function (ret) {
      		         			if ( callback != undefined ) {
      		         				callback(ret);
      		         			}
          	    			}, 
          	      dataType: "json",
          	      processData: false,
          	      type: "DELETE" }
          	      );    	
    } 

    my.newRecord = function( path, data, callback ) {
        DBServerPostJson( path, JSON.stringify(data), callback );  
    }

    my.deleteRecord = function( path, callback ) {
        DBServerDelete( path, callback );  
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
    	my.loadRecordsTemplate(
    			"/data/common/tags/",elementId,"snippet",
    			spec,null,null,null,
    			function (el) {
    				el.find("input[name=reference]").attr("value",path);
    				var select = el.find("select");
    				my.findRecords(
    						"/data/common/issues/",
    						function (data) {
    							for ( var i in data ) {
    								var tagname = data[i];
    								select.append("<option value='"+tagname._src+"'>"+tagname.name+"</option>");
    							}
    				});
    				el.find("form").submit( function() {
    					var selected_item = el.find("select option:selected").val();
    					var slug = path+"/"+selected_item;
    					slug = slug.replace(/\//g,"__");
    					my.newRecord("/data/common/tags/"+slug,
    								{ "reference" : path,
    						          "tag" : { "_ref" : selected_item } },
    						        function() {
    								    my.loadTagsForRecord(path,elementId); 
    						        } );
    					return false;
    				} );
    				el.find(".H-tag").click( function () {
    					var src = $(this).attr("rel");
    					my.deleteRecord( src, function() {
						    my.loadTagsForRecord(path,elementId); 
    					} );
    				} );
    			}
    	);
    }
    	
    return my; 
}());
