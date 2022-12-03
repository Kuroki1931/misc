import React from "react";
import { Cartesian3, ArcGisMapServerImageryProvider } from "cesium";
import { Viewer, Entity, ImageryLayer } from "resium";

const Resium = () => {
    return (
        <div>
            <Viewer>
                <Entity
                    name="Tokyo"
                    position={Cartesian3.fromDegreesArray([
                        139.767052, 35.681167,
                    ])}
                    point={{ pixelSize: 10 }}
                    description='Hello world'
                >
                </Entity>
            </Viewer>
        </div>
    )
}

export default Resium
