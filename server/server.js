var loopback = require('loopback');
var boot = require('loopback-boot');
var app = module.exports = loopback();

// Passport configurators..
var loopbackPassport = require('loopback-component-passport');
var PassportConfigurator = loopbackPassport.PassportConfigurator;
var passportConfigurator = new PassportConfigurator(app);

/*
 * body-parser is a piece of express middleware that
 *   reads a form's input and stores it as a javascript
 *   object accessible through `req.body`
 * Mostly useful to process POST requests
 */
var bodyParser = require('body-parser');
// to support JSON-encoded bodies
app.middleware('parse', bodyParser.json());
// to support URL-encoded bodies
app.middleware('parse', bodyParser.urlencoded({
	extended: true
}));

/**
 * Flash messages for passport
 *
 * Setting the failureFlash option to true instructs Passport to flash an
 * error message using the message given by the strategy's verify callback,
 * if any. This is often the best approach, because the verify callback
 * can make the most accurate determination of why authentication failed.
 */
var flash = require('express-flash');
var path = require('path');

// attempt to build the providers/passport config
var config = {};
try {
	config = require('../providers.json');
	secrets = require('../secrets.json');
} catch (err) {
	console.trace(err);
	process.exit(1); // fatal
}
// boot scripts mount components like REST API
boot(app, __dirname);

// The access token is only available after boot
app.middleware('auth', loopback.token({
  model: app.models.accessToken,
}));

app.middleware('session', loopback.session({
	secret: secrets.session,
	saveUninitialized: true,
	resave: true
}));
passportConfigurator.init();

// We need flash messages to see passport errors
app.use(flash());

passportConfigurator.setupModels({
	userModel: app.models.PLBUser,
	userIdentityModel: app.models.ForeignIdentity,
	userCredentialModel: app.models.ForeignCredential
});

for (var name in config) {
	var c = config[name];
	c.session = c.session !== false;
	passportConfigurator.configureProvider(name, c);
}
var ensureLoggedIn = require('connect-ensure-login').ensureLoggedIn;

app.get('/auth/fail', function (req, res, next) {
  res.status(403).send("Forbidden")	
});

app.get('/auth/success', ensureLoggedIn('/auth/fail'), function (req, res, next) {
  res.json({
      "user":req.user,
      "accessToken":req.UserAccessToken
      });
  console.log(req);
  app.models.user.find(function (req, res) {
      console.log(res);
      });
});

app.post('/auth/logout', function (req, res, next) {
  req.logout();
  res.status(204).send("No content")
});


function space(x) {
    var res = '';
    while(x--) res += ' ';
    return res;
}

// var express=require("express");
var router=app._router;

function listRoutes(){
    for (var i = 0; i < arguments.length;  i++) {
        if(arguments[i].stack instanceof Array){
            console.log('');
            arguments[i].stack.forEach(function(a){
                var route = a.route;
                if(route){
                    route.stack.forEach(function(r){
                        var method = r.method.toUpperCase();
                        console.log(method,space(8 - method.length),route.path);
                    })
                }
            });
        }
    }
}

listRoutes(router);

// Requests that get this far won't be handled
// by any middleware. Convert them into a 404 error
// that will be handled later down the chain.
app.use(loopback.urlNotFound());

// The ultimate error handler.
app.use(loopback.errorHandler());

app.start = function() {
	// start the web server
	return app.listen(function() {
		app.emit('started');
		console.log('Web server listening at: %s', app.get('url'));
	});
};

// start the server if `$ node server.js`
if (require.main === module) {
	app.start();
}
