import React from 'react'
import * as d3 from "d3";

import AxisBottom from './AxisBottom';
import AxisLeft from './AxisLeft';

const height = 500;
const width = 800;

const MARGIN = { top: 20, right: 40, bottom: 40, left: 40 };




export default function Chart() {
    const boundsWidth = width - MARGIN.right - MARGIN.left;
    const boundsHeight = height - MARGIN.top - MARGIN.bottom;

    const xScale = d3.scaleLinear().domain([0, 1238]).range([0, boundsWidth]);
    const yScale = d3.scaleLinear().domain([0, 100]).range([boundsHeight, 0]);

    return (
        <div className="flex  flex-col items-center p-10">
            <svg width={width} height={height} shapeRendering={"crispEdges"}>
                <rect width="100%" height="100%" fill="none" stroke="black" strokeWidth="2" />
                <g
                    width={boundsWidth}
                    height={boundsHeight}
                    transform={`translate(${[MARGIN.left, MARGIN.top].join(",")})`}
                    overflow={"visible"}
                >
                    <AxisLeft yScale={yScale} pixelsPerTick={30} />
                    <g transform={`translate(0, ${boundsHeight})`}>
                        <AxisBottom xScale={xScale} pixelsPerTick={60} />
                    </g>
                </g>
            </svg>
        </div>
    )
}
