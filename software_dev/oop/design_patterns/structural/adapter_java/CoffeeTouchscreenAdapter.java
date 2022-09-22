public class CoffeeTouchscreenAdapter implements CoffeeMachineInterface {

    private OldCoffeeMachine ocm;

    public CoffeeTouchscreenAdapter() {
        ocm = new OldCoffeeMachine();
    }

    public void chooseFirstSelection() {
        ocm.selectA();
    }

    public void chooseSecondSelection() {
        ocm.selectB();
    }

}