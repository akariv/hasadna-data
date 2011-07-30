The JavaScript Data Access Library
**********************************

The javascript library depends on the jQuery library, and can be fetched by adding the following lines to you HTML code:

.. code-block:: html

	<script type="text/javascript" src="http://api.yeda.us/data/static/jquery.min.js"></script>
	<script type="text/javascript" src="http://api.yeda.us/data/static/hasadna-api.js"></script>
	<link rel="stylesheet" type="text/css" href="http://api.yeda.us/data/static/hasadna-style.css"></link>

.. default-domain:: js

After document is loaded, you have the `H` module, which can be used to access the data.

Data Access Methods
-------------------

newRecord
+++++++++

Use this method to create a new record in the data store.

.. js:function:: H.newRecord(path, data[, callback])
   
   :param string path: The path to create on the server. The path must not end with a '/'.
   :param object data: A JSON object to set as this new element's data.
   :param function callback:
       Gets called when the operation is complete, with a boolean value indicating success.
   :returns: Nothing

deleteRecord
++++++++++++

Use this method to delete records from the data store.

.. js:function:: H.deleteRecord(path[, callback])
   
   :param string path: 
       The path to delete from the server. 
       If the path ends with a '/', all the elements in this directory will be removed; 
       otherwise, just a single record will be deleted.
   :param function callback:
       Gets called when the operation is complete, with a boolean value indicating success.
   :returns: Nothing

getRecord
+++++++++

Use this method to retrieve a single record from the data store.

.. js:function:: H.getRecord(path, callback)
   
   :param string path: 
       Path to a record to fetch from the server. 
       The path must not end with a '/'.
   :param function callback:
       Gets called when the operation is complete, with a JSON object containing the received data,
       or 'null' in case nothing was fetched (e.g. record was not found). 
   :returns: Nothing

findRecords
+++++++++++

Use this method to retrieve multiple records from the data store.

.. js:function:: H.getRecord(path, callback[, spec[, fields[, start[, limit]]]])
   
   :param string path: 
       Path for the records to fetch from the server. 
       The path must end with a '/'.
   :param function callback:
       Gets called when the operation is complete, with a JSON array containing the received records,
       or an empty array in case nothing was fetched (e.g. no record was not found).
   :param object spec:
       JSON object describing the query filter (in MongoDB format).  
   :param list fields:
       JSON array conatining the names of the required fields.
       Omitting this parameter or passing 'null' will cause all fields to be fetched.  
   :param int start:
       Start record to fetch.
       Defaults to '0'.
   :param int limit:
       Maximum number of records to fetch.
       Defaults to '10'.
   :returns: Nothing

countRecordsTemplate
++++++++++++++++++++

Count records matching a specific filter and use a template to display the count.

.. js:function:: H.countRecordsTemplate(path,elementId,template[, spec[, fields[, callback]]])
   
   :param string path: 
       Path for the records to fetch from the server. 
       The path must end with a '/'.
   :param string elementId:
       A DOM element with this id will be used to hold the fetched information.
   :param string template:
       The name of the template to be used in the server to render the information.
   :param object spec:
       JSON object describing the query filter (in MongoDB format).  
   :param list fields:
       JSON array conatining the names of the required fields.
       Omitting this parameter or passing 'null' will cause all fields to be fetched.  
   :param function callback:
       Gets called when the operation is complete, with the jQuery selector for the element containing the rendered data. 
   :returns: Nothing

loadRecordTemplate
++++++++++++++++++

Use this method to retrieve multiple records from the data store, and render them using a server template.

.. js:function:: H.loadRecordTemplate(path,elementId,template[, callback])
   
   :param string path: 
       Path for the record to fetch from the server. 
       The path must not end with a '/'.
   :param string elementId:
       A DOM element with this id will be used to hold the fetched information.
   :param string template:
       The name of the template to be used in the server to render the information.
   :param function callback:
       Gets called when the operation is complete, with the jQuery selector for the element containing the rendered data. 
   :returns: Nothing

loadRecordsTemplate
+++++++++++++++++++

Use this method to retrieve multiple records from the data store, and render them using a server template.

.. js:function:: H.loadRecordsTemplate(path,elementId,template[, spec[, fields[, start[, limit[, callback]]]]])
   
   :param string path: 
       Path for the records to fetch from the server. 
       The path must end with a '/'.
   :param string elementId:
       A DOM element with this id will be used to hold the fetched information.
   :param string template:
       The name of the template to be used in the server to render the information.
   :param object spec:
       JSON object describing the query filter (in MongoDB format).  
   :param list fields:
       JSON array conatining the names of the required fields.
       Omitting this parameter or passing 'null' will cause all fields to be fetched.  
   :param int start:
       Start record to fetch.
       Defaults to '0'.
   :param int limit:
       Maximum number of records to fetch.
       Defaults to '10'.
   :param function callback:
       Gets called when the operation is complete, with the jQuery selector for the element containing the rendered data. 
   :returns: Nothing


Login Header
------------

In case you want to support users logging in to your site, you should load the Sadna's standard login header into the page.
Once the header is loaded, you may access the 'H_login_data' object, which contains the following fields:

H_login_data
++++++++++++

.. js:attribute:: key
   
   The openID token for the logged in user.

loadLoginHeader
+++++++++++++++

Use this method to load the Sadna's standard login header into the page.

.. js:function:: H.loadLoginHeader(elementId)
   
   :param string elementId:
       A DOM element with this id will be used to hold the login header.
   :returns: Nothing
    
Tagging Module Methods
----------------------

.. note: TBW - also move to a separate file

loadTagsForRecord
+++++++++++++++++

Use this method to retrieve tags for a single record.

.. js:function:: H.loadTagsForRecord(path, elementId)
   
   :param string path: 
       Path for the records to fetch tags for.
   :param string elementId:
   	   An element with this id will be filled with the corresponding tags.

Starring Module Methods
-----------------------

.. note: TBW - also move to a separate file

loadStarsForRecord
++++++++++++++++++

Use this method to retrieve the starring widget for a single record.

.. js:function:: H.loadStarsForRecord(path, elementId)
   
   :param string path: 
       Path for the records to fetch tags for.
   :param string elementId:
   	   An element with this id will be filled with the corresponding tags.

   	       	
Example Code
------------
 
 .. code-block:: html
 
	<html>
	
	<head>
		<script type="text/javascript" src="http://api.yeda.us/data/static/jquery.min.js"></script>
		<script type="text/javascript" src="http://api.yeda.us/data/static/hasadna-api.js"></script>
		<link rel="stylesheet" type="text/css" href="http://api.yeda.us/data/static/hasadna-style.css"></link>
		<style type="text/css">
			body { direction: rtl; }
			
			ol.H-budget-list { list-style: none; }
			ul.H-budget-item { list-style: none; }
			li.H-budget-item-src { display: none; }
			li.H-budget-item-code {
				font: italic normal 12px Courier,monospace;
				display: inline-block; 
			}
			li.H-budget-item-title {
				font: normal bold 14px Helvetica,sans-serif;
				display: inline-block;
				color: blue; 
			}
			li.H-budget-item-title:hover {
				text-decoration: underline;
				cursor: pointer;
			}
			li.H-budget-item-year { display: none; }
						
		</style>
	</head>
	
	<script type="text/javascript">
	
	var year = 2005;
	var code = "00";
	
	var my =  H;
	
	function refresh_list() {
		H.loadRecordsTemplate("/data/gov/mof/budget/","budget","list",
							  { "code" : { "$regex" : "^"+code+"(..)?$" } , 
	 				    	  "year" : year },
				 			  null,0,100,
				 			  function () {
	 				 			var src = $("li.H-budget-item-src:first").html();
	 				    		H.loadTagsForRecord( src, "tags" );
	 				    		H.loadStarsForRecord( src, "stars" );
	 				    	  });
	}
	
	$( function () {
	
		$("#test1").html("loaded!");
	
		H.loadLoginHeader("login");
				
		$("#year-selection").val(""+year);
		$("#year-selection").change( function() {
			year = parseInt( $("#year-selection").val() );
			refresh_list();
		} );
	
		$("li.H-budget-item-title").live("click", function() {
			code = $(this).parent().find("li.H-budget-item-code").html();
			refresh_list();
		} );
		
		refresh_list();
	} );
	
	</script>
	
	<body dir="rtl">
	
		<div id="login"></div>
		
		<select id="year-selection">
		  <option value="1992">1992</option>
		  <option value="1993">1993</option>
		  <option value="1994">1994</option>
		  <option value="1995">1995</option>
		  <option value="1996">1996</option>
		  <option value="1997">1997</option>
		  <option value="1998">1998</option>
		  <option value="1999">1999</option>
		  <option value="2000">2000</option>
		  <option value="2001">2001</option>
		  <option value="2002">2002</option>
		  <option value="2003">2003</option>
		  <option value="2004">2004</option>
		  <option value="2005">2005</option>
		  <option value="2006">2006</option>
		  <option value="2007">2007</option>
		  <option value="2008">2008</option>
		  <option value="2009">2009</option>
		  <option value="2000">2000</option>
		  <option value="2011">2011</option>
		  <option value="2012">2012</option>
		</select>
		
		<div id="tags"></div>
	
		<div id="stars"></div>
	
		<div id="budget"></div>
	
	</body>
	
	</html>