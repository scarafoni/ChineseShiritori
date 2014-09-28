/*
 * Big Red Hacks RHINE Javascript Reference Client
 * Required libraries: jQuery ( <script type="text/javascript" src="http://code.jquery.com/jquery-1.11.1.min.js>"></script> )
 * Returns strings on which GET requests can be run (through e.g. jQuery).
 */

function _conv(es) {
    if (typeof es == "object")
        return es.join();
    else
        return es;
}

function _conv2(es) {
    return es.map(function(l) { return "(" + l.join() + ")"; });
}

function gen(api_key, call) {
    return "http://api.rhine.io:8080/" + api_key + "/" + call;
}

function distance(api_key, entity1, entity2) {
    return gen(api_key, "distance/" + _conv(entity1) + "/" + _conv(entity2));
}

function best_match(api_key, tomatch, possibilities, num) {
    return gen(api_key, "best_match/" + _conv(tomatch) + "/" + _conv2(possibilities) + "/" + String(num));
}

function synonym_check(api_key, entity1, entity2) {
    return gen(api_key, "synonym_check/" + entity1 + "/" + entity2);
}

function entity_extraction(api_key, text) {
    return gen(api_key, "entity_extraction/");
    // Add {'rawText': < text >} as POST data.
}

function closest_entities(api_key, entity) {
    return gen(api_key, "closest_entities/" + entity);
}
