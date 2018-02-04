var metalsmith = require('metalsmith');
var markdown = require('metalsmith-markdown');
var layouts = require('metalsmith-layouts');
var assets = require('metalsmith-assets');
var handlebars = require('handlebars');
var collections = require('metalsmith-collections');
var pagination = require('metalsmith-pagination');
var permalinks = require('metalsmith-permalinks');
var moremeta = require('./lib/metalsmith-moremeta');
var tags = require('metalsmith-tags');
var author = require('metalsmith-author');
var lunr = require('metalsmith-lunr');
var serve = require('metalsmith-serve');
var watch = require('metalsmith-watch');
var feedjs = require('metalsmith-feed');
//var feedjs = require('metalsmith-feed-js');
var minify = require('metalsmith-html-minifier');
//var lunr_ = require('lunr');
//require('lunr-languages/lunr.stemmer.support')(lunr_);
//require('lunr-languages/lunr.no')(lunr_);

metalsmith(__dirname)
  .metadata({
    site: {
      name: 'Faith Family Church',
      description: "FFC Wesbsite and Podcast, Taylors, SC, Jesus, Christianity, faith, Rhema",
      url: 'https://myffc.org',
//      author: 'info@myffc.org',
      title: 'Faith Family Church',
      subtitle: 'Faith Family Church, Taylors, SC'
    }
  })
  .source('./src')
  .destination('./public')
  .clean(true)
  .use(collections({
      sermons: {
        pattern: 'sermons/**/*.md',
        sortBy: 'date',
        reverse: true
        },
        lastArticles: {
          sortBy: 'date',
          limit: 10
        },
        metadata: {
          layout:   'sermon.html'
        },
      posts: {
        pattern: 'posts/**/*.md',
        sortBy: 'date',
        reverse: true
        },
        lastArticles: {
          sortBy: 'date',
          limit: 10
        }
      }))
  .use(markdown({
    gfm: true,
    tables: true,
    breaks: false,
    pedantic: false,
    sanitize: true,
    smartLists: true,
    smartypants: true
  }))
  .use(assets({
      source: 'src/assets', // relative to the working directory
      destination: './assets' // relative to the build directory
  }))
  .use(permalinks({
      relative: false,
      pattern: ':mainCollection/:title',
  }))
  .use(pagination({
    "collections.sermons": {
    	"perPage": 10,
      "layout": "sermons.html",
      "first": "sermons/index.html",
      "noPageOne": true,
      "path": "sermons/:num/index.html"
    }
  }))
  .use(tags({
    // yaml key for tag list in you pages
    handle: 'tags',
    // path for result pages
    path: "topics/:tag/index.html",
    //pathPage: "topics/:tag/:num/index.html",
    //perPage: 10,
    // layout to use for tag listing
    layout:'tags.html',
    // provide posts sorted by 'date' (optional)
    sortBy: 'date',
    // sort direction (optional)
    reverse: true,
    // skip updating metalsmith's metadata object.
    // useful for improving performance on large blogs
    // (optional)
    //skipMetadata: true,
    // Any options you want to pass to the [slug](https://github.com/dodo/node-slug) package.
    // Can also supply a custom slug function.
    //slug: function(tag) { return tag.toLowerCase() }
    slug: {mode: 'rfc3986'}
  }))
  .use(author({ // make sure it comes after collections
    collection: 'sermons'
    //authors: {
    //  john: {
    //    name: 'John Lennon',
    //    url: 'http://somesite.com',
    //    twitter: '@johnlennon'
    //  },
    //  paul: {
    //    name: 'Paul McCartney',
    //    url: 'http://somesite.com',
    //    twitter: '@paulmccartney'
    //  }
    //}
  }))
.use(lunr({
  ref: 'title',
  indexPath: 'searchIndex.json',
  fields: {
      contents: 1,
      author: 10
  },
//  pipelineFunctions: [
//    lunr_.trimmer,
//    lunr_.no.stopWordFilter,
//    lunr_.no.stemmer
//	  ],
  preprocess: function(content) {
    // Replace all occurrences of __title__ with the current file's title metadata.
    return content.replace(/__title__/g, this.title);
  }
}))
  .use(minify())
  .use(feedjs({
    collection: 'sermons',
    copyright: "2017 Faith Family Church, Taylors, SC",
    language: "en-us",
    category: "Christianity",
    explicit: "no",
    limit: false,
    destination: "rss.xml"
  }))
  .use(feedjs({
    collection: 'sermons',
    copyright: "2017 Faith Family Church, Taylors, SC",
    language: "en-us",
    category: "Christianity",
    explicit: "no",
    destination: "itunes.xml",
    subtitle: "Faith Family Church, Taylors, SC",
    limit: 50,
    image_url: "https://myffc.org/assets/images/logo_current.jpg",
    custom_namespaces: {
      'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
    },
    custom_elements: [
      {'itunes:subtitle': 'to know Jesus to make Jesus known'},
      {'itunes:author': 'Faith Family Church'},
      {'itunes:summary': 'Follow us every Sunday as we discover the truths from the Word of God. Look for our podcast in the Podcasts app or in the iTunes Store'},
      {'itunes:owner': [
        {'itunes:name': 'FFC'},
        {'itunes:email': 'info@myffc.org'}
      ]},
      {'itunes:image': {
        _attr: {
          href: 'https://myffc.org/assets/images/logo_current.jpg'
        }
      }},
      {'itunes:category': [
        {_attr: {
          text: 'Religion & Spirituality'
        }}
      ]},
      {'itunes:explicit': 'no'}
    ]

  }))
  .use(layouts({
            engine: 'handlebars',
            directory: './layouts',
            default: 'article.html',
            pattern: ["*/*/*html","*/*html","*html"],
            partials: {
              header: 'partials/header',
              footer: 'partials/footer'
            }
        }))
  .use(serve({
    host: '0.0.0.0',
    port: 8080,
    verbose: true
  }))
  .use(watch({
    paths: {
      "${source}/**/*": true,
      "layout/**/*": "**/*",
    }
  }))
  .build(function (err) {
    if (err) {
      console.log(err);
    }
    else {
      console.log('myffc built!');
    }
  });
