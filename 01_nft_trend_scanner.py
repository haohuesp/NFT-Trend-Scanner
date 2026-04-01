# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

import json
import typing


class NFTTrendScanner(gl.Contract):
    has_scanned: bool
    trend_score: str
    top_collection: str
    analysis: str
    scan_url: str

    def __init__(self, scan_url: str):
        self.has_scanned = False
        self.trend_score = "50"
        self.top_collection = "unknown"
        self.analysis = "Awaiting first scan"
        self.scan_url = scan_url

    @gl.public.write
    def scan_trends(self) -> typing.Any:

        if self.has_scanned:
            return "Already scanned"

        def nondet() -> str:
            response = gl.nondet.web.render(self.scan_url, mode="text")
            print(response)

            task = f"""You are an NFT market analyst.
            Analyze the following NFT marketplace data:
            {response[:2000]}

            Respond with the following JSON format:
            {{
                "trend_score": str,
                "top_collection": str,
                "market_sentiment": str,
                "summary": str
            }}
            trend_score: a number 0-100 as string, where 0 means dead market, 100 means extremely hot.
            top_collection: name of the most trending NFT collection.
            market_sentiment: one of BEARISH, NEUTRAL, BULLISH.
            summary: one sentence about current NFT market trends.
            It is mandatory that you respond only using the JSON format above,
            nothing else. Don't include any other words or characters,
            your output must be only JSON without any formatting prefix or suffix.
            This result should be perfectly parsable by a JSON parser without errors.
            """
            result = gl.nondet.exec_prompt(task).replace("```json", "").replace("```", "")
            print(result)
            return json.dumps(json.loads(result), sort_keys=True)

        result_json = json.loads(gl.eq_principle.strict_eq(nondet))

        self.has_scanned = True
        self.trend_score = str(result_json["trend_score"])
        self.top_collection = result_json["top_collection"]
        self.analysis = result_json["summary"]

        return result_json