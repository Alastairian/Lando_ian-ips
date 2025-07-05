import { LogosCore } from "./logosCore";
import { PathosCore } from "./pathosCore";

export class TwineCognition {
  logos: LogosCore;
  pathos: PathosCore;

  constructor() {
    this.logos = new LogosCore();
    this.pathos = new PathosCore();
  }

  process(input: number[]): number[] {
    const pathosMarkers = this.pathos.process(input);
    // Use Pathos output to bias Logos processing
    const logosResult = this.logos.process([...input, ...pathosMarkers]);
    // Feedback: update Pathos with Logos error or uncertainty signals
    return logosResult;
  }
}