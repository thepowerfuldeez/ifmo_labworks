package ru.ifmo.lab3.validator;

import javax.faces.application.FacesMessage;
import javax.faces.component.UIComponent;
import javax.faces.context.FacesContext;
import javax.faces.validator.FacesValidator;
import javax.faces.validator.Validator;
import javax.faces.validator.ValidatorException;
import java.math.BigDecimal;
import java.util.regex.Pattern;

@FacesValidator("ru.ifmo.DoubleRangeValidator")
public class DoubleRangeValidator implements Validator {
    private static final String PATTERN = "^\\s*(\\+|-)?[0-9]+(?:\\.[0-9]+)?(?:[eE](?:\\+|-)?[0-9]+)?\\s*$";

    @Override
    public void validate(FacesContext facesContext, UIComponent uiComponent, Object o) throws ValidatorException {
        Pattern p = Pattern.compile(PATTERN);
        if (!p.matcher(o.toString()).matches()) {
            FacesMessage message = new FacesMessage("Not a double number!");
            message.setSeverity(FacesMessage.SEVERITY_ERROR);
            throw new ValidatorException(message);
        }

        BigDecimal left = new BigDecimal(-5);
        BigDecimal right = new BigDecimal(5);

        BigDecimal number = new BigDecimal(o.toString());

        if (number.compareTo(left) < 0 || number.compareTo(right) > 0) {
            FacesMessage message = new FacesMessage("Number must be in range from -5 to 5");
            message.setSeverity(FacesMessage.SEVERITY_ERROR);
            throw new ValidatorException(message);
        }
    }
}
