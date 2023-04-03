
  <body>
    <h1>Main.py</h1>
    <p>This is a Python script that uses the <code>discord</code>, <code>requests</code>, and <code>BeautifulSoup</code> libraries to scrape product prices from amazon and send a notification to a Discord channel when the price drops below a certain threshold.</p>
    <h2>Dependencies</h2>
    <ul>
      <li><code>discord</code></li>
      <li><code>requests</code></li>
      <li><code>beautifulsoup4</code></li>
    </ul>
    <h2>Usage</h2>
    <p>To use this script, you will need to set up a Discord bot and obtain an API token. Once you have the token, create a text file "token.txt" and place your token inside </p>
    <p>The script provides the following commands:</p>
    <ul>
      <li><code>$add &lt;URL&gt; &lt;targetPrice&gt;</code>: adds a new product URL and target price to the list</li>
      <li><code>$print</code>: prints the list of product URLs and target prices</li>
      <li><code>$test &lt;arg&gt;</code>: sends a test message to the Discord channel</li>
    </ul>
    <h2>How it works</h2>
    <p>Once an hour, It'll check for prices and ping any channel named "product-alerts" if the price is less than the threshold you set</p>
    <h2>Future plans</h2>
    <p>I wrote this bot because i felt the need to learn python, plus i needed something to keep track of prices automatically. I may consider switching to writing thew bot in typescript, as it seem like a far superior language to write this in, plus I want to learn typescript as well. Hosted on heroku free tier (might switch ??). if you have any questions feel free to DM me on discord DNWMN#8684 </p>
