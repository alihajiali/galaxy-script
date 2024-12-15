const { chromium } = require("playwright")
const express = require("express")
const dotenv = require("dotenv")
const app = express()
app.use(express.json())

dotenv.config();

const scrapeData = async (url) => {
    const browser = await chromium.launch({ headless: true })
    const page = await browser.newPage()
    await page.goto(url)
    const content = await page.content()
    await browser.close()
    return content
}

app.get('/', async (req, res) => {
    const token = req.headers['authorization']
    if (!token) {
        return res.status(401).send("Missing authentication token.")
    }
    console.log(process.env.AUTH_TOKEN, token)
    if (token !== process.env.AUTH_TOKEN) {
        return res.status(403).send("Invalid authentication token.")
    }
    const { url } = req.query
    if (!url) {
        return res.status(400).send("Missing 'url' query parameter.")
    }
    try {
        const data = await scrapeData(url)
        res.send(data)
    } catch (error) {
        console.error("Error during scraping:", error)
        res.status(500).send("An error occurred while scraping.")
    }
})

app.listen(3000, () => {
    console.log("app is running")
})
