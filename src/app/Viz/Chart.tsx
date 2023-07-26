import React from 'react'
import * as d3 from "d3";

import AxisBottom from './AxisBottom';

const height = 500;
const width = 800;

const MARGIN = { top: 30, right: 30, bottom: 50, left: 50 };




export default function Chart() {
    const boundsWidth = width - MARGIN.right - MARGIN.left;
    const boundsHeight = height - MARGIN.top - MARGIN.bottom;

    const xScale = d3.scaleLinear().domain([0, 10]).range([0, boundsWidth]);
    const yScale = d3.scaleLinear().domain([0, 11]).range([boundsHeight, 0]);
    
    return (
        <div>
            <svg width={width} height={height}>
                <rect width="100%" height="100%" fill="none" stroke="black" strokeWidth="2" />
                <g transform={`translate(0, ${boundsHeight})`}>
                    <AxisBottom xScale={xScale} pixelsPerTick={60} />
                </g>
            </svg>
        </div>
    )
}
