package core;

import java.io.*;

import org.apache.http.*;
import org.apache.http.client.methods.*;
import org.apache.http.impl.client.*;
import org.apache.http.util.*;
import org.json.*;

public class Rhine {
    private static String url = "http://api.rhine.io:8080";
    
    private CloseableHttpClient client = HttpClients.createDefault();
    private String apikey;
    
    public Rhine(String apikey) {
        this.apikey = apikey;
    }
    
    private static String convert(String[] in) {
    	String res = "";
    	for (int i = 0; i < in.length; i++) { 
    		res += in[i]; 
    		if (i < in.length - 1) res += ",";
    	}
    	return res;
    }

    private JSONObject call(String data) {
        HttpGet method = new HttpGet(Rhine.url + "/" + this.apikey + "/" + data);
        CloseableHttpResponse r = null;
        try {
        	r = this.client.execute(method);
            HttpEntity body = r.getEntity();
            JSONObject response = new JSONObject(EntityUtils.toString(body));
            EntityUtils.consume(body);
            return response;
        }
        catch (JSONException e) { System.err.println("JSON Error: " + e.getMessage()); e.printStackTrace(); return null; }
        catch (IOException e) { System.err.println("IO Error: " + e.getMessage()); e.printStackTrace(); return null; }
        finally { try { r.close(); } catch (Exception e) {} }
    }

    public double distance(String[] entityListOne, String[] entityListTwo) {
        try {
        	return this.call("distance/" + Rhine.convert(entityListOne) + "/" + Rhine.convert(entityListTwo)).getDouble("distance");
        }
        catch (JSONException e) { System.err.println("JSON Error: " + e.getMessage()); e.printStackTrace(); return -1; }
    }

    public boolean synonym_check(String entityOne, String entityTwo) {
        try {
        	return this.call("synonym_check/" + entityOne + "/" + entityTwo).getBoolean("synonym");
        }
        catch (JSONException e) { System.err.println("JSON Error: " + e.getMessage()); e.printStackTrace(); return false; }
    }

    public String[] closest_entities(String entity) {
    	JSONArray arr = null;
        try {
        	arr = this.call("closest_entities/" + entity).getJSONArray("closest_entities");
        }
        catch (JSONException e) { System.err.println("JSON Error: " + e.getMessage()); e.printStackTrace(); return null; }
        String[] res = new String[arr.length()];
        try {
        	for (int i = 0; i < arr.length(); i++) { res[i] = arr.getString(i); }
        }
        catch (JSONException e) { System.err.println("JSON Error: " + e.getMessage()); e.printStackTrace(); return null; }
        return res;
    }

    public String[] entity_extraction(String text) {
    	text = text.replaceAll(" ", "%20");
    	JSONArray arr = null;
        try {
        	arr = this.call("entity_extraction/" + text).getJSONArray("entities");
        }
        catch (JSONException e) { System.err.println("JSON Error: " + e.getMessage()); e.printStackTrace(); return null; }
        String[] res = new String[arr.length()];
        try {
        	for (int i = 0; i < arr.length(); i++) { res[i] = arr.getString(i); }
        }
        catch (JSONException e) { System.err.println("JSON Error: " + e.getMessage()); e.printStackTrace(); return null; }
        return res;
    }
}



